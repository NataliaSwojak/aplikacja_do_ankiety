import pandas as pd


# Wczytanie pliku CSV z uwzględnieniem separatora średnika
df = pd.read_csv('35__welcome_survey_cleaned.csv', sep=';')

# Utworzenie nowej ramki danych z przetworzonymi danymi
processed_df = df.copy()

# Zmiana nazw kolumn w nowej ramce danych
processed_df.rename(columns={
    'age': 'Wiek',
    'edu_level': 'Poziom wykształcenia',
    'fav_animals': 'Ulubione zwierzęta',
    'fav_place': 'Ulubione miejsce',
    'gender': 'Płeć',
    'hobby_art': 'Hobby_Sztuka',
    'hobby_books': 'Hobby_Książki',
    'hobby_movies': 'Hobby_Filmy',
    'hobby_other': 'Hobby_Inne',
    'hobby_sport': 'Hobby_Sport',
    'hobby_video_games': 'Hobby_Gry video',
    'industry': 'Branża',
    'learning_pref_books': 'Nauka_Książki',
    'learning_pref_chatgpt': 'Nauka_Chatgpt',
    'learning_pref_offline_courses': 'Nauka_Kursy offline',
    'learning_pref_online_courses': 'Nauka_Kursy online',
    'learning_pref_personal_projects': 'Nauka_Projekty indywidualne',
    'learning_pref_teaching': 'Nauka_Nauczanie',
    'learning_pref_teamwork': 'Nauka_Praca zespołowa',
    'learning_pref_workshops': 'Nauka_Warsztaty',
    'motivation_career': 'Motywacja_Kariera',
    'motivation_challenges': 'Motywacja_Wyzwania',
    'motivation_creativity_and_innovation': 'Motywacja_Kreatywność i innowacja',
    'motivation_money_and_job': 'Motywacja_Pieniądze i praca',
    'motivation_personal_growth': 'Motywacja_Rozwój osobisty',
    'motivation_remote': 'Motywacja_Praca zdalna',
    'sweet_or_salty': 'Słodki czy słony',
    'years_of_experience': 'Lata doświadczenia'
}, inplace=True)

# Zamiana wartości 'unknown' na 'Brak danych' w kolumnie 'Wiek'
processed_df['Wiek'] = processed_df['Wiek'].replace('unknown', 'Brak danych')

# Zamiana wartości 1 na 'Kobiety' a 0 na 'Mężczyźni' w kolumnie 'Płeć'
processed_df['Płeć'] = processed_df['Płeć'].replace({1: 'Kobieta', 0: 'Mężczyzna'})

# Zamiana wartości NaN na 'Brak danych' w kolumnach 'Ulubione miejsce', 'Płeć', 'Branża', 'Słodki czy słony' i 'Lata doświadczenia'
processed_df['Ulubione miejsce'] = processed_df['Ulubione miejsce'].fillna('Brak danych')
processed_df['Płeć'] = processed_df['Płeć'].fillna('Brak danych')
processed_df['Branża'] = processed_df['Branża'].replace(['Brak', None], 'Brak danych')
processed_df['Słodki czy słony'] = processed_df['Słodki czy słony'].replace(['sweet', 'salty', None], ['Słodki', 'Słony', 'Brak danych'])
processed_df['Lata doświadczenia'] = processed_df['Lata doświadczenia'].fillna('Brak danych')

# Eksport przetworzonej ramki danych, aby była dostępna po zaimportowaniu modułu
__all__ = ['processed_df']
