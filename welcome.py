import streamlit as st

def show_welcome():
    st.title("Witaj w aplikacji do analizy danych z ankiety!")

    st.write(""" 
    Aplikacja została zaprojektowana, aby umożliwić łatwe i interaktywne badanie różnych relacji i zależności w zbiorze danych zawierającym wyniki ankiet przeprowadzonych wśród uczestników kursu "Od zera do AI". 

    ### Co znajdziesz w aplikacji?

    Aplikacja składa się z kilku kluczowych sekcji, które pomogą dokładnie przeanalizować dostępne dane:

    1. **Eksploracja Danych**:
        - W tej sekcji możesz szybko zapoznać się z podstawowymi informacjami o danych.
        - Znajdziesz tu statystyki opisowe, które pomogą zrozumieć rozkłady zmiennych oraz wyłapać potencjalne anomalie lub braki danych.
        - Poznasz ogólną strukturę zbioru danych, co pozwoli Ci na lepsze zrozumienie dalszych analiz.

    2. **Wizualizacja Danych**:
        - Tutaj możesz tworzyć histogramy i wykresy słupkowe, które pomogą wizualnie przeanalizować rozkłady zmiennych oraz relacje między nimi.
        - Ta sekcja pozwala na tworzenie intuicyjnych i przejrzystych wizualizacji, które ułatwią Ci interpretację wyników.

    3. **Analiza Relacji**:
        - W tej części możesz przeprowadzić analizę zależności między zmiennymi.
        - Dostępna jest interaktywna macierz korelacji, która pozwala na identyfikację silnych i słabych zależności między zmiennymi.
        - Możesz także zobaczyć szczegółowe wykresy przedstawiające średnie, mediany oraz odchylenia standardowe dla wybranych zmiennych.
        - Ta sekcja jest idealna do odkrywania, jak różne cechy wpływają na siebie nawzajem.

    ### Jak korzystać z aplikacji?

    - Skorzystaj z menu po lewej stronie, aby nawigować po różnych częściach aplikacji.
    - Każda sekcja jest interaktywna i zaprojektowana z myślą o intuicyjnym użytkowaniu, dzięki czemu możesz szybko przejść od eksploracji danych do bardziej zaawansowanych analiz.
    - Zastosuj różne filtry i opcje wyboru, aby skupić się na interesujących Cię aspektach danych i odkryć ukryte zależności.

    ### Dodatkowe Informacje:
    - Aby lepiej zrozumieć, jak różne zmienne zostały zakodowane, zapoznaj się z informacjami o kodowaniu dostępnymi w sekcji "Analiza Relacji".
    - Wszystkie wykresy i analizy można dostosować do własnych potrzeb, co pozwala na elastyczne podejście do badania danych.

    Mam nadzieję, że aplikacja pomoże Ci w pełni wykorzystać potencjał dostępnych danych i odkryć cenne wnioski. Powodzenia!
             
    Natalia
    """)
