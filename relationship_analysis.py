import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from data_processed import processed_df  # Import przetworzonej ramki danych

# Funkcja do grupowania branż
def group_branches(df):
    branch_mapping = {
        'IT': 'IT',
        'Brak danych': 'Brak danych',
        'Finanse': 'Finanse',
        'Zdrowie': 'Zdrowie',
        'Edukacja': 'Edukacja',
        'Usługi': 'Usługi',
        'Logistyka': 'Logistyka',
        'Energetyka': 'Energetyka',
        'Automotive': 'Automotive',
        'Marketing': 'Marketing'
    }
    df['Branża (Grupy)'] = df['Branża'].map(branch_mapping).fillna('Pozostałe')
    return df

# Funkcja do ustawienia kolejności kategorii
def reorder_categories(df):
    category_order = {
        'Płeć': ["Kobieta", "Mężczyzna"],
        'Wiek': ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65"],
        'Poziom wykształcenia': ["Podstawowe", "Średnie", "Wyższe"],
        'Lata doświadczenia': ["0-2", "3-5", "6-10", "11-15", ">=16"],
        'Ulubione zwierzęta': ["Koty", "Psy", "Koty i Psy", "Inne", "Brak ulubionych"],
        'Ulubione miejsce': ["Nad wodą", "W górach", "W lesie", "Inne"],
        'Słodki czy słony': ["Słodki", "Słony"],
        'Branża (Grupy)': ['IT', 'Brak danych', 'Finanse', 'Zdrowie', 'Edukacja', 'Usługi', 'Logistyka', 'Energetyka', 'Automotive', 'Marketing', 'Pozostałe']
    }
    
    df_reordered = df.copy()
    for column, order in category_order.items():
        if column in df_reordered.columns:
            df_reordered[column] = pd.Categorical(df_reordered[column], categories=order, ordered=True)
    
    return df_reordered

# Funkcja do zamiany danych kategorycznych na liczbowe
def encode_categories(df):
    df_encoded = df.copy()
    mappings = {}
    for column in df_encoded.columns:
        if df_encoded[column].dtype == 'object' or isinstance(df_encoded[column].dtype, pd.CategoricalDtype):
            df_encoded[column] = df_encoded[column].replace("Brak danych", None)
            df_encoded = df_encoded.dropna(subset=[column])
            valid_values = df_encoded[column].cat.categories if isinstance(df_encoded[column].dtype, pd.CategoricalDtype) else df_encoded[column].unique()
            mapping = {category: code for code, category in enumerate(valid_values)}
            mappings[column] = mapping
            df_encoded[column] = df_encoded[column].map(mapping).astype(int)
        elif any(df_encoded[column].name.startswith(prefix) for prefix in ['Motywacja_', 'Nauka_', 'Hobby_']):
            valid_values = [0, 1]  # Zakładamy, że kolumny są binarne (0/1)
            mapping = {value: value for value in valid_values}
            mappings[column] = mapping
    return df_encoded, mappings

def show_relationship_analysis():
    st.title("Analiza relacji między zmiennymi")

    st.markdown("""
    ## Jak korzystać z zakładki Analiza relacji?

    Zakładka "Analiza relacji" pozwala na interaktywną analizę zależności między różnymi zmiennymi w danych. 
    Możesz wybrać zmienne na osiach X i Y, aby zrozumieć, jak te zmienne są ze sobą powiązane. W tej sekcji masz dostęp do dwóch narzędzi analizy:

    1. **Interaktywna Macierz Korelacji**:
        - Narzędzie to pozwala na wizualizację współzależności między różnymi zmiennymi w danych.
        - Macierz korelacji przedstawia współczynniki korelacji między wybranymi zmiennymi, co pozwala na szybkie zidentyfikowanie silnych lub słabych zależności.
        - W macierzy znajdują się zmienne takie jak: **Płeć**, **Wiek**, **Poziom wykształcenia**, **Lata doświadczenia**, **Słodki czy słony**, a także zmienne związane z **Motywacją**, **Nauką** i **Hobby**.
        - Zmienna jest przedstawiona jako liczba, a kolory w macierzy wskazują na siłę i kierunek korelacji (od ujemnej do dodatniej).

    2. **Średnia, Mediana oraz Wąsy**:
        - Po wybraniu zmiennych na osiach X i Y, generowany jest wykres przedstawiający średnią, medianę oraz odchylenie standardowe i rozstęp międzykwartylowy dla wybranych zmiennych.
        - **Średnia** jest reprezentowana jako niebieski słupek, z zaznaczonym odchyleniem standardowym w postaci "wąsów".
        - **Mediana** jest reprezentowana jako pomarańczowy słupek, z zaznaczonymi pierwszym i trzecim kwartylem jako "wąsy".
        - Dzięki temu wykresowi możesz zidentyfikować, jak wybrane zmienne (np. wiek, poziom wykształcenia, motywacja) rozkładają się względem siebie w różnych grupach.
        - Wykresy stanowią uzupełnienie dla analizy z zakładki Wizualizacja danych.
    """)

    st.markdown("""
    ### Informacje o kodowaniu zmiennych:
    - **Płeć**: Kobieta (0), Mężczyzna (1)
    - **Wiek**: <18 (0), 18-24 (1), 25-34 (2), 35-44 (3), 45-54 (4), 55-64 (5), >=65 (6)
    - **Poziom wykształcenia**: Podstawowe (0), Średnie (1), Wyższe (2)
    - **Lata doświadczenia**: 0-2 (0), 3-5 (1), 6-10 (2), 11-15 (3), >=16 (4)
    - **Słodki czy słony**: Słodki (0), Słony (1)
    - **Motywacja**: Nie (0), Tak (1)
    - **Nauka**: Nie (0), Tak (1)
    - **Hobby**: Nie (0), Tak (1)
    """)

    df_grouped = group_branches(processed_df)
    df_reordered = reorder_categories(df_grouped)
    df_encoded, mappings = encode_categories(df_reordered)

    correlation_columns = [col for col in df_encoded.columns if col not in ['Branża', 'Branża (Grupy)', 'Ulubione zwierzęta', 'Ulubione miejsce']]
    ordered_correlation_columns = ['Płeć', 'Wiek', 'Poziom wykształcenia', 'Lata doświadczenia', 'Słodki czy słony'] + \
                                  [col for col in correlation_columns if col.startswith('Motywacja_')] + \
                                  [col for col in correlation_columns if col.startswith('Nauka_')] + \
                                  [col for col in correlation_columns if col.startswith('Hobby_')]

    st.subheader("Interaktywna Macierz Korelacji")

    try:
        corr_matrix = df_encoded[ordered_correlation_columns].corr().round(2)
        fig = px.imshow(corr_matrix, text_auto=True, aspect="auto", color_continuous_scale="RdBu_r")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Wystąpił błąd podczas generowania macierzy korelacji: {e}")

    x_options = ['Płeć', 'Wiek', 'Poziom wykształcenia', 'Branża (Grupy)', 'Lata doświadczenia', 'Ulubione zwierzęta', 'Ulubione miejsce', 'Słodki czy słony'] + \
                [col for col in df_encoded.columns if col.startswith('Motywacja_')] + \
                [col for col in df_encoded.columns if col.startswith('Nauka_')] + \
                [col for col in df_encoded.columns if col.startswith('Hobby_')]

    y_options = ['Płeć', 'Wiek', 'Poziom wykształcenia', 'Lata doświadczenia', 'Słodki czy słony'] + \
                [col for col in df_encoded.columns if col.startswith('Motywacja_')] + \
                [col for col in df_encoded.columns if col.startswith('Nauka_')] + \
                [col for col in df_encoded.columns if col.startswith('Hobby_')]

    x_variable = st.selectbox("Wybierz zmienną na osi X", x_options)
    y_variable = st.selectbox("Wybierz zmienną na osi Y", y_options)

    if x_variable and y_variable:
        st.subheader(f"Wykres średniej oraz mediany wraz z odchyleniem standardowym i rozstępem kwartylowym dla {x_variable} i {y_variable}")

        try:
            group_stats = df_encoded.groupby(x_variable)[y_variable].agg(
                mean='mean', std='std', median='median', q1=lambda x: x.quantile(0.25), q3=lambda x: x.quantile(0.75)
            )

            group_stats = group_stats.dropna(subset=['median', 'q1', 'q3'])

            x_labels = [k for k, v in sorted(mappings[x_variable].items(), key=lambda item: item[1]) if v in group_stats.index]

            fig, ax = plt.subplots(figsize=(10, 6))
            width = 0.35
            indices = range(len(group_stats))

            ax.bar(indices, group_stats['mean'], width, label='Średnia', color='blue', alpha=0.6, yerr=group_stats['std'])
            ax.bar([i + width for i in indices], group_stats['median'], width, label='Mediana', color='orange', alpha=0.6, 
                   yerr=[group_stats['median'] - group_stats['q1'], group_stats['q3'] - group_stats['median']])

            ax.set_xlabel(x_variable)
            ax.set_ylabel(f'{y_variable} (Średnia i Mediana)')
            ax.set_xticks([i + width / 2 for i in indices])
            ax.set_xticklabels(x_labels, rotation=45)

            if y_variable in mappings:
                y_tick_labels = {v: k for k, v in mappings[y_variable].items()}
                ax.set_yticks(sorted(y_tick_labels.keys()))
                ax.set_yticklabels([y_tick_labels[tick] for tick in sorted(y_tick_labels.keys())])

            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Wystąpił błąd podczas generowania wykresu: {e}")

    else:
        st.warning("Proszę wybrać zmienną dla osi X i osi Y.")

def main():
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Wybierz analizę", ["Analiza relacji"])

    if page == "Analiza relacji":
        show_relationship_analysis()

if __name__ == "__main__":
    main()
