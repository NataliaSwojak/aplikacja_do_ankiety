import streamlit as st
import pandas as pd
from data_processed import processed_df
from filters import get_filters, update_filters, reset_filters

def show_exploration():
    st.title("Eksploracja danych")

     # Dodanie opisu instrukcji dla użytkownika
    st.markdown("""
    ## Jak korzystać z zakładki Eksploracja?
    W tej zakładce możesz analizować dane poprzez filtrowanie oraz przeglądanie statystyk. 
    
    1. **Filtry**: W panelu bocznym znajdziesz różne opcje filtrów, które pozwolą Ci zawęzić dane do interesujących Cię kategorii.
    2. **Zastosuj/Resetuj**: Po dokonaniu wyborów w filtrach kliknij "Zastosuj", aby przefiltrować dane, lub "Resetuj", aby przywrócić domyślne ustawienia.
    3. **Tabela wyników**: Po zastosowaniu filtrów zobaczysz przefiltrowane dane w postaci tabeli.
    4. **Podsumowanie statystyczne**: Na dole strony znajdziesz podsumowanie statystyczne dla wybranych kategorii, które pokazuje najczęstsze i najrzadsze wartości oraz ilość brakujących danych.
    5. **Komunikaty**: Aplikacja wyświetli komunikaty, jeśli nie zostaną wybrane żadne opcje w filtrach lub jeśli dla wybranych kategorii nie ma dostępnych danych.
    """)

    # Inicjalizacja przetworzonych danych
    df = processed_df.copy()

    # Pobierz istniejące filtry lub ustaw domyślne
    filters = get_filters()

    with st.sidebar:
        st.header("Filtry")

        # Tworzenie formularza do zbierania opcji filtrów
        with st.form(key='filter_form_1'):
            selected_plec = st.multiselect(
                "Płeć", ["Wszystkie", "Kobieta", "Mężczyzna", "Brak danych"],
                default=filters['selected_plec']
            )
            selected_wiek = st.multiselect(
                "Wiek", ["Wszystkie", "<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65", "Brak danych"],
                default=filters['selected_wiek']
            )
            selected_edukacja = st.multiselect(
                "Poziom wykształcenia", ["Wszystkie", "Podstawowe", "Średnie", "Wyższe"],
                default=filters['selected_edukacja']
            )

            branza_unique_values = sorted(df['Branża'].dropna().unique())
            if "Brak danych" in branza_unique_values:
                branza_unique_values.remove("Brak danych")
            branza_options = ["Wszystkie"] + branza_unique_values + ["Brak danych"]
            selected_branza = st.multiselect(
                "Branża", branza_options,
                default=filters['selected_branza']
            )

            selected_doswiadczenie = st.multiselect(
                "Lata doświadczenia", ["Wszystkie", "0-2", "3-5", "6-10", "11-15", ">=16", "Brak danych"],
                default=filters['selected_doswiadczenie']
            )

            motywacja_columns = {col: col.replace("Motywacja_", "") for col in df.columns if col.startswith('Motywacja_')}
            selected_motywacja = st.multiselect(
                "Motywacje", ["Wszystkie"] + sorted(motywacja_columns.values()),
                default=filters['selected_motywacja']
            )

            nauka_columns = {col: col.replace("Nauka_", "") for col in df.columns if col.startswith('Nauka_')}
            selected_nauka = st.multiselect(
                "Preferencje Nauki", ["Wszystkie"] + sorted(nauka_columns.values()),
                default=filters['selected_nauka']
            )

            hobby_columns = {col: col.replace("Hobby_", "") for col in df.columns if col.startswith('Hobby_')}
            hobby_values = sorted(hobby_columns.values())
            if "Inne" in hobby_values:
                hobby_values.remove("Inne")
            hobby_options = ["Wszystkie"] + hobby_values + ["Inne"]
            selected_hobby = st.multiselect(
                "Hobby", hobby_options,
                default=filters['selected_hobby']
            )

            selected_zwierzeta = st.multiselect(
                "Ulubione zwierzęta", ["Wszystkie", "Koty", "Psy", "Koty i Psy", "Inne", "Brak ulubionych"],
                default=filters['selected_zwierzeta']
            )
            selected_miejsce = st.multiselect(
                "Ulubione miejsce", ["Wszystkie", "Nad wodą", "W górach", "W lesie", "Inne", "Brak danych"],
                default=filters['selected_miejsce']
            )
            selected_slodki_sony = st.multiselect(
                "Słodki czy słony", ["Wszystkie", "Słodki", "Słony", "Brak danych"],
                default=filters['selected_slodki_sony']
            )

            col1, col2 = st.columns([1, 1])
            with col1:
                submit_button = st.form_submit_button(label='Zastosuj')
            with col2:
                reset_button = st.form_submit_button(label='Resetuj')

    if submit_button:
        # Zaktualizuj filtry w session_state, zastępując stare wartości nowymi
        update_filters(
            selected_plec, selected_wiek, selected_edukacja, selected_branza,
            selected_doswiadczenie, selected_motywacja, selected_nauka,
            selected_hobby, selected_zwierzeta, selected_miejsce, selected_slodki_sony
        )
        st.rerun()  # Odświeżenie strony po zastosowaniu filtrów

    if reset_button:
        reset_filters()  # Resetowanie filtrów do wartości domyślnych
        st.rerun()  # Odświeżenie strony po resetowaniu

    missing_filters = []
    df_empty_due_to_filters = False

    # Sprawdzenie i filtracja danych na podstawie wybranych filtrów
    if not selected_plec:
        missing_filters.append("Płeć")
    elif "Wszystkie" not in filters['selected_plec']:
        df = df[df['Płeć'].isin(filters['selected_plec'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_wiek:
        missing_filters.append("Wiek")
    elif "Wszystkie" not in filters['selected_wiek']:
        df = df[df['Wiek'].isin(filters['selected_wiek'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_edukacja:
        missing_filters.append("Poziom wykształcenia")
    elif "Wszystkie" not in filters['selected_edukacja']:
        df = df[df['Poziom wykształcenia'].isin(filters['selected_edukacja'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_branza:
        missing_filters.append("Branża")
    elif "Wszystkie" not in filters['selected_branza']:
        df = df[df['Branża'].isin(filters['selected_branza'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_doswiadczenie:
        missing_filters.append("Lata doświadczenia")
    elif "Wszystkie" not in filters['selected_doswiadczenie']:
        df = df[df['Lata doświadczenia'].isin(filters['selected_doswiadczenie'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_motywacja:
        missing_filters.append("Motywacje")
    elif "Wszystkie" not in filters['selected_motywacja']:
        selected_columns = [key for key, value in motywacja_columns.items() if value in filters['selected_motywacja']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_nauka:
        missing_filters.append("Preferencje Nauki")
    elif "Wszystkie" not in filters['selected_nauka']:
        selected_columns = [key for key, value in nauka_columns.items() if value in filters['selected_nauka']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_hobby:
        missing_filters.append("Hobby")
    elif "Wszystkie" not in filters['selected_hobby']:
        selected_columns = [key for key, value in hobby_columns.items() if value in filters['selected_hobby']]
        df = df[(df[selected_columns] == 1).any(axis=1)]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_zwierzeta:
        missing_filters.append("Ulubione zwierzęta")
    elif "Wszystkie" not in filters['selected_zwierzeta']:
        df = df[df['Ulubione zwierzęta'].isin(filters['selected_zwierzeta'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_miejsce:
        missing_filters.append("Ulubione miejsce")
    elif "Wszystkie" not in filters['selected_miejsce']:
        df = df[df['Ulubione miejsce'].isin(filters['selected_miejsce'])]
        if df.empty:
            df_empty_due_to_filters = True

    if not selected_slodki_sony:
        missing_filters.append("Słodki czy słony")
    elif "Wszystkie" not in filters['selected_slodki_sony']:
        df = df[df['Słodki czy słony'].isin(filters['selected_slodki_sony'])]
        if df.empty:
            df_empty_due_to_filters = True

    if df_empty_due_to_filters:
        st.warning("Brak danych do wyświetlenia dla wybranych kategorii.")
    elif missing_filters:
        st.warning(f"Brak wyboru kategorii dla następujących filtrów: {', '.join(missing_filters)}")
    else:
        st.subheader("Przefiltrowane dane")
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.write(f"Liczba wyświetlanych rekordów: {len(df)}")

        def calculate_occurrences(column):
            counts = df[column].value_counts()
            if 'Brak danych' in counts:
                missing_count = counts['Brak danych']
                counts = counts.drop('Brak danych')
            else:
                missing_count = 0
            return counts, missing_count

        def calculate_most_least_frequent(counts, apply_100_percent_rule=False, apply_zero_percent_rule=False):
            if len(counts) == 0:
                return "Brak", "Brak", "Brak", "Brak"

            max_count = counts.max()
            min_count = counts.min()

            most_frequent_values = counts[counts == max_count].index.tolist()
            most_frequent_percent = round((max_count / counts.sum()) * 100, 1) if counts.sum() > 0 else 0.0

            if apply_100_percent_rule and most_frequent_percent == 100:
                rarest = "Brak"
                rarest_percent = 0.0
            else:
                rarest_values = counts[counts == min_count].index.tolist()
                rarest_percent = round((min_count / counts.sum()) * 100, 1) if counts.sum() > 0 else 0.0

                if len(rarest_values) <= 40:
                    rarest = "\n".join(rarest_values)
                else:
                    rarest = "Wiele wartości"

            if len(most_frequent_values) <= 40:
                most_frequent = "\n".join(most_frequent_values)
            else:
                most_frequent = "Wiele wartości"

            if most_frequent == rarest:
                rarest = "Brak"
                rarest_percent = 0.0

            if apply_zero_percent_rule and most_frequent_percent == 0:
                most_frequent = "Brak"
                rarest = "Brak"
                rarest_percent = 0.0

            return most_frequent, most_frequent_percent, rarest, rarest_percent

        st.subheader("Podsumowanie statystyczne")

        stats = pd.DataFrame(columns=[
            'Cecha',
            'Unikalnych wartości',
            'Najczęstsza wartość', '[% Najczęstsza]',
            'Najrzadsza wartość', '[% Najrzadsza]',
            'Brak danych', '[% Brak danych]'
        ], dtype="object")

        columns_to_analyze = [
            'Płeć', 'Wiek', 'Poziom wykształcenia', 'Branża', 'Lata doświadczenia',
            'Ulubione zwierzęta', 'Ulubione miejsce', 'Słodki czy słony'
        ]

        for column in columns_to_analyze:
            counts, missing_count = calculate_occurrences(column)
            apply_100_percent_rule = column in [
                'Płeć', 'Wiek', 'Poziom wykształcenia', 'Branża', 'Lata doświadczenia',
                'Ulubione zwierzęta', 'Ulubione miejsce', 'Słodki czy słony'
            ]
            apply_zero_percent_rule = column in ['Ulubione miejsce', 'Słodki czy słony']
            if len(counts) > 0:
                most_frequent, most_frequent_percent, rarest, rarest_percent = calculate_most_least_frequent(
                    counts, apply_100_percent_rule, apply_zero_percent_rule)
            else:
                most_frequent, most_frequent_percent, rarest, rarest_percent = "Brak", "0.0", "Brak", "0.0"

            temp_df = pd.DataFrame([{
                'Cecha': column,
                'Unikalnych wartości': len(counts),
                'Najczęstsza wartość': most_frequent,
                '[% Najczęstsza]': most_frequent_percent,
                'Najrzadsza wartość': rarest,
                '[% Najrzadsza]': rarest_percent,
                'Brak danych': missing_count,
                '[% Brak danych]': round((missing_count / len(df)) * 100, 1) if len(df) > 0 else "Brak"
            }])

            stats = pd.concat([stats, temp_df], ignore_index=True)

        def calculate_group_stats(columns, group_name=None):
            if group_name in ['Hobby', 'Motywacje', 'Preferencje Nauki']:
                group_sums = df[columns].sum()
                max_value = group_sums.max()
                min_value = group_sums.min()

                missing_count = df[columns].apply(lambda row: all(row == 0), axis=1).sum()
                non_missing_count = len(df) - missing_count

                most_frequent_values = group_sums[group_sums == max_value].index.tolist()
                rarest_values = group_sums[group_sums == min_value].index.tolist()

                if len(most_frequent_values) <= 40:
                    most_frequent = "\n".join(most_frequent_values).replace('Hobby_', '').replace('Motywacja_', '').replace('Nauka_', '')
                else:
                    most_frequent = "Wiele wartości"

                if len(rarest_values) <= 40:
                    rarest = "\n".join(rarest_values).replace('Hobby_', '').replace('Motywacja_', '').replace('Nauka_', '')
                else:
                    rarest = "Wiele wartości"

                mode_percent = round((max_value / len(df)) * 100, 1) if len(df) > 0 else 0
                rarest_percent = round((min_value / len(df)) * 100, 1) if len(df) > 0 else 0
                unique_count = len(group_sums[group_sums > 0])

                missing_percent = round((missing_count / len(df)) * 100, 1) if len(df) > 0 else 0

                if mode_percent == 0:
                    most_frequent = "Brak"
                    rarest = "Brak"

                return pd.Series([
                    unique_count,
                    most_frequent, mode_percent,
                    rarest, rarest_percent,
                    missing_count, missing_percent
                ], index=[
                    'Unikalnych wartości',
                    'Najczęstsza wartość', '[% Najczęstsza]',
                    'Najrzadsza wartość', '[% Najrzadsza]',
                    'Brak danych', '[% Brak danych]'
                ])
            else:
                group_data = df[columns].apply(pd.Series.value_counts)
                total_count = len(df)

                if 'Brak danych' in group_data.index:
                    missing_count = group_data.loc['Brak danych'].sum()
                    group_data = group_data.drop('Brak danych')
                else:
                    missing_count = 0

                non_missing_count = total_count - missing_count

                most_frequent = group_data.idxmax().iloc[0] if not group_data.empty else "Brak"
                rarest = group_data.idxmin().iloc[0] if not group_data.empty else "Brak"
                mode_percent = round((group_data.max().iloc[0] / non_missing_count) * 100, 1) if non_missing_count > 0 else "Brak"
                rarest_percent = round((group_data.min().iloc[0] / non_missing_count) * 100, 1) if non_missing_count > 0 else "Brak"
                unique_count = group_data.index.nunique()
                missing_percent = round((missing_count / total_count) * 100, 1) if total_count > 0 else 0

                most_frequent = "Brak" if pd.isna(most_frequent) else most_frequent
                rarest = "Brak" if pd.isna(rarest) else rarest

                return pd.Series([
                    unique_count,
                    most_frequent, mode_percent,
                    rarest, rarest_percent,
                    missing_count, missing_percent
                ], index=[
                    'Unikalnych wartości',
                    'Najczęstsza wartość', '[% Najczęstsza]',
                    'Najrzadsza wartość', '[% Najrzadsza]',
                    'Brak danych', '[% Brak danych]'
                ])

        # Obliczanie statystyk dla grup (Hobby, Motywacje, Preferencje Nauki)
        for group_name, columns in {
            'Hobby': list(hobby_columns.keys()),
            'Motywacje': list(motywacja_columns.keys()),
            'Preferencje Nauki': list(nauka_columns.keys())
        }.items():
            group_stats = calculate_group_stats(columns, group_name)
            stats = pd.concat([stats, pd.DataFrame([{'Cecha': group_name, **group_stats}])], ignore_index=True)

        # Ustawienie odpowiedniej kolejności wierszy
        stats['order'] = stats['Cecha'].map({f: i for i, f in enumerate([
            'Płeć', 'Wiek', 'Poziom wykształcenia', 'Branża', 'Lata doświadczenia', 
            'Motywacje', 'Preferencje Nauki', 'Hobby',
            'Ulubione zwierzęta', 'Ulubione miejsce', 'Słodki czy słony'
        ])})
        stats = stats.sort_values('order').drop('order', axis=1).reset_index(drop=True)

        # Wyświetlenie tabeli ze statystykami
        st.dataframe(stats.astype(str), use_container_width=True, hide_index=True)

        # Dodanie opisu interpretacji dla użytkownika
        st.subheader("Jak interpretować tabelę?")
        st.markdown("""
        - **Cecha**: To kolumna opisująca różne kategorie, takie jak płeć, wiek, poziom wykształcenia itp. 
        - **Unikalnych wartości**: Liczba różnych unikalnych wartości występujących w danej cesze. Na przykład, w kolumnie płeć mogą występować wartości takie jak 'Kobieta', 'Mężczyzna', 'Brak danych'. Jeśli przefiltrujesz dane tylko do kategorii 'Kobieta', wówczas unikalnych wartości będzie 1.
        - **Najczęstsza wartość**: Wartość, która występuje najczęściej w danej cesze. Na przykład, jeśli najwięcej osób ma poziom wykształcenia "Wyższe", to jest to najczęstsza wartość. Jeśli kilka wartości będzie kwalifikowala się jako występujące najczęściej, wówczas zostaną one wymienione w tabeli wszystkie.
        - **[% Najczęstsza]**: Procent wszystkich danych w tej cesze, które mają najczęstszą wartość. Dotyczy osobno każdej wartości, jeśli jako najczęstsze kwalifikowanych jest ich kilka.
        - **Najrzadsza wartość**: Wartość, która występuje najrzadziej w danej cesze. Może to być na przykład specyficzne hobby lub unikalna kombinacja motywacji. Jeśli kilka wartości będzie kwalifikowala się jako występujące najrzadziej, wówczas zostaną one wymienione w tabeli wszystkie.
        - **[% Najrzadsza]**: Procent wszystkich danych w tej cesze, które mają najrzadszą wartość. Dotyczy osobno każdej wartości, jeśli jako najrzadsze kwalifikowanych jest ich kilka.
        - **Brak danych**: Liczba brakujących danych (puste lub "Brak danych") dla danej cechy.
        - **[% Brak danych]**: Procent danych, które są brakujące w tej cesze w odniesieniu do wszystkich danych.

        Tabela pomaga w zrozumieniu, jakie wartości dominują w różnych cechach i gdzie mogą występować luki w danych. Dzięki temu możesz lepiej analizować strukturę swoich danych oraz podejmować decyzje dotyczące dalszej analizy lub uzupełnienia brakujących informacji.
        """)

# Uruchomienie funkcji
show_exploration()
