import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_processed import processed_df
from split_charts import (
    plot_gender_split_bar_chart,
    plot_education_split_bar_chart,
    plot_age_split_bar_chart,
    plot_grouped_bar_chart_1
)
from split_branches_experience import (
    plot_branch_split_bar_chart,
    plot_experience_split_bar_chart,
    plot_grouped_bar_chart_2
)
from split_favourite import (
    plot_animals_split_bar_chart,
    plot_places_split_bar_chart,
    plot_sweet_salty_split_bar_chart,
    plot_grouped_bar_chart_3
)
from filters import get_filters, update_filters, reset_filters

def reset_split_options(exclude_key=None):
    split_options = [
        'split_by_gender', 'split_by_edukation', 'split_by_age', 'split_by_branch',
        'split_by_experience', 'split_by_animals', 'split_by_places', 'split_by_sweet_salty'
    ]
    for key in split_options:
        if key != exclude_key:
            st.session_state[key] = False

def initialize_session_state():
    default_states = {
        'split_by_gender': False,
        'split_by_edukation': False,
        'split_by_age': False,
        'split_by_branch': False,
        'split_by_experience': False,
        'split_by_animals': False,
        'split_by_places': False,
        'split_by_sweet_salty': False,
        'active_split': 'no_split',
        'filters': get_filters()
    }
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value

def show_visualization():
    st.title("Wizualizacja danych")

    # Inicjalizacja session state
    initialize_session_state()

 # Dodanie opisu instrukcji dla użytkownika
    st.markdown("""
    ## Jak korzystać z zakładki Wizualizacja?
    W tej zakładce możesz tworzyć różnorodne wykresy w celu analizy danych. 
    
    1. **Opcje podziału**: W panelu bocznym znajdziesz przyciski umożliwiające podzielenie wykresów według różnych kategorii, takich jak płeć, wiek, wykształcenie itp.
    2. **Filtry**: Możesz także zastosować filtry, aby zawęzić dane do interesujących Cię kategorii. Jeśli nie wybierzesz żadnych opcji w filtrze, dane nie zostaną przefiltrowane.
    3. **Zastosuj/Resetuj**: Po dokonaniu wyborów w filtrach kliknij "Zastosuj", aby zaktualizować wykresy, lub "Resetuj", aby przywrócić domyślne ustawienia.
    4. **Komunikaty**: Aplikacja wyświetli komunikaty, jeśli nie zostaną wybrane żadne opcje w filtrach lub jeśli dla wybranych kategorii nie ma dostępnych danych.
    """)
    
    df = processed_df.copy()
    filters = st.session_state['filters']

    st.sidebar.header("Opcje wizualizacji")

    # Funkcja do obsługi wyboru podziału
    def handle_split_selection(split_key):
        reset_split_options(split_key)
        st.session_state[split_key] = True
        st.session_state['active_split'] = split_key

    # Przyciski do wyboru podziału
    st.sidebar.button("Bez podziału", on_click=lambda: handle_split_selection('no_split'))
    st.sidebar.button("Podziel na płeć", on_click=lambda: handle_split_selection('split_by_gender'))
    st.sidebar.button("Podziel na wiek", on_click=lambda: handle_split_selection('split_by_age'))
    st.sidebar.button("Podziel na wykształcenie", on_click=lambda: handle_split_selection('split_by_edukation'))
    st.sidebar.button("Podziel na branżę", on_click=lambda: handle_split_selection('split_by_branch'))
    st.sidebar.button("Podziel na lata doświadczenia", on_click=lambda: handle_split_selection('split_by_experience'))
    st.sidebar.button("Podziel na ulubione zwierzęta", on_click=lambda: handle_split_selection('split_by_animals'))
    st.sidebar.button("Podziel na ulubione miejsce", on_click=lambda: handle_split_selection('split_by_places'))
    st.sidebar.button("Podziel na słodki czy słony", on_click=lambda: handle_split_selection('split_by_sweet_salty'))

    missing_filters = []

    with st.sidebar:
        st.header("Filtry")
        with st.form(key='filter_form_2'):
            selected_plec = st.multiselect(
                "Płeć", ["Wszystkie", "Kobieta", "Mężczyzna", "Brak danych"],
                default=filters['selected_plec']
            )
            if not selected_plec:
                missing_filters.append("Płeć")

            selected_wiek = st.multiselect(
                "Wiek", ["Wszystkie", "<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65", "Brak danych"],
                default=filters['selected_wiek']
            )
            if not selected_wiek:
                missing_filters.append("Wiek")

            selected_edukacja = st.multiselect(
                "Poziom wykształcenia", ["Wszystkie", "Podstawowe", "Średnie", "Wyższe"],
                default=filters['selected_edukacja']
            )
            if not selected_edukacja:
                missing_filters.append("Poziom wykształcenia")

            branza_unique_values = sorted(df['Branża'].dropna().unique())
            if "Brak danych" in branza_unique_values:
                branza_unique_values.remove("Brak danych")
            branza_options = ["Wszystkie"] + branza_unique_values + ["Brak danych"]
            selected_branza = st.multiselect(
                "Branża", branza_options,
                default=filters['selected_branza']
            )
            if not selected_branza:
                missing_filters.append("Branża")

            selected_doswiadczenie = st.multiselect(
                "Lata doświadczenia", ["Wszystkie", "0-2", "3-5", "6-10", "11-15", ">=16", "Brak danych"],
                default=filters['selected_doswiadczenie']
            )
            if not selected_doswiadczenie:
                missing_filters.append("Lata doświadczenia")

            motywacja_columns = {col: col.replace("Motywacja_", "") for col in df.columns if col.startswith('Motywacja_')}
            selected_motywacja = st.multiselect(
                "Motywacje", ["Wszystkie"] + sorted(motywacja_columns.values()),
                default=filters['selected_motywacja']
            )
            if not selected_motywacja:
                missing_filters.append("Motywacje")

            nauka_columns = {col: col.replace("Nauka_", "") for col in df.columns if col.startswith('Nauka_')}
            selected_nauka = st.multiselect(
                "Preferencje Nauki", ["Wszystkie"] + sorted(nauka_columns.values()),
                default=filters['selected_nauka']
            )
            if not selected_nauka:
                missing_filters.append("Preferencje Nauki")

            hobby_columns = {col: col.replace("Hobby_", "") for col in df.columns if col.startswith('Hobby_')}
            hobby_values = sorted(hobby_columns.values())
            if "Inne" in hobby_values:
                hobby_values.remove("Inne")
            hobby_options = ["Wszystkie"] + hobby_values + ["Inne"]
            selected_hobby = st.multiselect(
                "Hobby", hobby_options,
                default=filters['selected_hobby']
            )
            if not selected_hobby:
                missing_filters.append("Hobby")

            selected_zwierzeta = st.multiselect(
                "Ulubione zwierzęta", ["Wszystkie", "Koty", "Psy", "Koty i Psy", "Inne", "Brak ulubionych"],
                default=filters['selected_zwierzeta']
            )
            if not selected_zwierzeta:
                missing_filters.append("Ulubione zwierzęta")

            selected_miejsce = st.multiselect(
                "Ulubione miejsce", ["Wszystkie", "Nad wodą", "W górach", "W lesie", "Inne", "Brak danych"],
                default=filters['selected_miejsce']
            )
            if not selected_miejsce:
                missing_filters.append("Ulubione miejsce")

            selected_slodki_sony = st.multiselect(
                "Słodki czy słony", ["Wszystkie", "Słodki", "Słony", "Brak danych"],
                default=filters['selected_slodki_sony']
            )
            if not selected_slodki_sony:
                missing_filters.append("Słodki czy słony")

            col1, col2 = st.columns([1, 1])
            with col1:
                submit_button = st.form_submit_button(label='Zastosuj')
            with col2:
                reset_button = st.form_submit_button(label='Resetuj')

    if reset_button:
        reset_filters()
        st.rerun()  # Odświeżenie interfejsu po zresetowaniu filtrów

    if submit_button:
        # Zaktualizuj filtry
        update_filters(
            selected_plec, selected_wiek, selected_edukacja, selected_branza,
            selected_doswiadczenie, selected_motywacja, selected_nauka, selected_hobby,
            selected_zwierzeta, selected_miejsce, selected_slodki_sony
        )
        st.rerun()  # Odświeżenie interfejsu po zastosowaniu filtrów

    df_empty_due_to_filters = False

    # Zastosowanie filtrów do danych
    if "Wszystkie" not in filters['selected_plec'] and filters['selected_plec']:
        df = df[df['Płeć'].isin(filters['selected_plec'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_wiek'] and filters['selected_wiek']:
        df = df[df['Wiek'].isin(filters['selected_wiek'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_edukacja'] and filters['selected_edukacja']:
        df = df[df['Poziom wykształcenia'].isin(filters['selected_edukacja'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_branza'] and filters['selected_branza']:
        df = df[df['Branża'].isin(filters['selected_branza'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_doswiadczenie'] and filters['selected_doswiadczenie']:
        df = df[df['Lata doświadczenia'].isin(filters['selected_doswiadczenie'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_motywacja'] and filters['selected_motywacja']:
        selected_columns = [key for key, value in motywacja_columns.items() if value in filters['selected_motywacja']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_nauka'] and filters['selected_nauka']:
        selected_columns = [key for key, value in nauka_columns.items() if value in filters['selected_nauka']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_hobby'] and filters['selected_hobby']:
        selected_columns = [key for key, value in hobby_columns.items() if value in filters['selected_hobby']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_zwierzeta'] and filters['selected_zwierzeta']:
        df = df[df['Ulubione zwierzęta'].isin(filters['selected_zwierzeta'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_miejsce'] and filters['selected_miejsce']:
        df = df[df['Ulubione miejsce'].isin(filters['selected_miejsce'])]
        if df.empty:
            df_empty_due_to_filters = True

    if "Wszystkie" not in filters['selected_slodki_sony'] and filters['selected_slodki_sony']:
        df = df[df['Słodki czy słony'].isin(filters['selected_slodki_sony'])]
        if df.empty:
            df_empty_due_to_filters = True

    if missing_filters:
        st.warning(f"Brak wyboru kategorii dla następujących filtrów: {', '.join(missing_filters)}")
    elif df_empty_due_to_filters:
        st.warning("Brak danych do wyświetlenia dla wybranych kategorii.")
    else:
        st.subheader("Wykresy słupkowe i histogramy")

        def plot_bar_chart(data, column, title):
            if st.session_state['split_by_gender']:
                plot_gender_split_bar_chart(data, column, title)
            elif st.session_state['split_by_edukation']:
                plot_education_split_bar_chart(data, column, title)
            elif st.session_state['split_by_age']:
                plot_age_split_bar_chart(data, column, title)
            elif st.session_state['split_by_branch']:
                plot_branch_split_bar_chart(data, column, title)
            elif st.session_state['split_by_experience']:
                plot_experience_split_bar_chart(data, column, title)
            elif st.session_state['split_by_animals']:
                plot_animals_split_bar_chart(data, column, title)
            elif st.session_state['split_by_places']:
                plot_places_split_bar_chart(data, column, title)
            elif st.session_state['split_by_sweet_salty']:
                plot_sweet_salty_split_bar_chart(data, column, title)
            else:
                fig, ax = plt.subplots(figsize=(14, 10))
                data[column].value_counts().sort_values(ascending=True).plot(kind='barh', ax=ax, color='blue', label=column)
                ax.set_title(title, fontsize=18)
                ax.set_xlabel('Liczba', fontsize=14)
                ax.set_ylabel(column, fontsize=14)
                ax.legend()
                plt.xticks(fontsize=12)
                plt.yticks(fontsize=12)
                plt.tight_layout()
                st.pyplot(fig)

        def plot_vertical_bar_chart(data, column, title, categories_order):
            if st.session_state['split_by_gender']:
                plot_gender_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_edukation']:
                plot_education_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_age']:
                plot_age_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_branch']:
                plot_branch_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_experience']:
                plot_experience_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_animals']:
                plot_animals_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_places']:
                plot_places_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            elif st.session_state['split_by_sweet_salty']:
                plot_sweet_salty_split_bar_chart(data, column, title, categories_order, sort_data=False, is_vertical=True)
            else:
                fig, ax = plt.subplots(figsize=(14, 10))
                ordered_data = data[column].value_counts().reindex(categories_order)
                ordered_data.plot(kind='bar', ax=ax, color='blue', label=column)
                ax.set_title(title, fontsize=18)
                ax.set_xlabel(column, fontsize=14)
                ax.set_ylabel('Liczba', fontsize=14)
                ax.legend()
                plt.xticks(rotation=0, fontsize=12)
                plt.yticks(fontsize=12)
                plt.tight_layout()
                st.pyplot(fig)

        plot_bar_chart(df, 'Płeć', 'Rozkład płci')
        plot_vertical_bar_chart(df, 'Wiek', 'Rozkład wieku', ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65", "Brak danych"])
        plot_bar_chart(df, 'Poziom wykształcenia', 'Rozkład poziomu wykształcenia')
        plot_bar_chart(df, 'Branża', 'Rozkład branż')
        plot_vertical_bar_chart(df, 'Lata doświadczenia', 'Rozkład lat doświadczenia', ["0-2", "3-5", "6-10", "11-15", ">=16", "Brak danych"])

        if any([st.session_state['split_by_gender'], st.session_state['split_by_edukation'], st.session_state['split_by_age']]):
            plot_grouped_bar_chart_1(df, list(motywacja_columns.keys()), 'Rozkład Motywacji', 'Motywacja_')
            plot_grouped_bar_chart_1(df, list(nauka_columns.keys()), 'Rozkład Preferencji Nauki', 'Nauka_')
            plot_grouped_bar_chart_1(df, list(hobby_columns.keys()), 'Rozkład Hobby', 'Hobby_')
        elif any([st.session_state['split_by_experience'], st.session_state['split_by_branch']]):
            plot_grouped_bar_chart_2(df, list(motywacja_columns.keys()), 'Rozkład Motywacji', 'Motywacja_')
            plot_grouped_bar_chart_2(df, list(nauka_columns.keys()), 'Rozkład Preferencji Nauki', 'Nauka_')
            plot_grouped_bar_chart_2(df, list(hobby_columns.keys()), 'Rozkład Hobby', 'Hobby_')
        elif any([st.session_state['split_by_animals'], st.session_state['split_by_places'], st.session_state['split_by_sweet_salty']]):
            plot_grouped_bar_chart_3(df, list(motywacja_columns.keys()), 'Rozkład Motywacji', 'Motywacja_')
            plot_grouped_bar_chart_3(df, list(nauka_columns.keys()), 'Rozkład Preferencji Nauki', 'Nauka_')
            plot_grouped_bar_chart_3(df, list(hobby_columns.keys()), 'Rozkład Hobby', 'Hobby_')
        else:
            plot_grouped_bar_chart_1(df, list(motywacja_columns.keys()), 'Rozkład Motywacji', 'Motywacja_')
            plot_grouped_bar_chart_1(df, list(nauka_columns.keys()), 'Rozkład Preferencji Nauki', 'Nauka_')
            plot_grouped_bar_chart_1(df, list(hobby_columns.keys()), 'Rozkład Hobby', 'Hobby_')

        plot_bar_chart(df, 'Ulubione zwierzęta', 'Rozkład ulubionych zwierząt')
        plot_bar_chart(df, 'Ulubione miejsce', 'Rozkład ulubionych miejsc')
        plot_bar_chart(df, 'Słodki czy słony', 'Rozkład preferencji Słodki czy Słony')

show_visualization()
