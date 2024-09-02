import streamlit as st
from welcome import show_welcome
from data_exploration import show_exploration
from data_visualization import show_visualization
from relationship_analysis import show_relationship_analysis  


# Funkcja wymuszająca jednorazowe odświeżenie strony
def refresh_page_once():
    if st.session_state.get('refresh_count', 0) == 0:
        st.session_state['refresh_count'] = 1
        st.rerun()

# Sprawdzenie, czy strona powinna być odświeżona
if "refresh_count" not in st.session_state:
    st.session_state["refresh_count"] = 0
    refresh_page_once()

# Tworzenie rozwijanego menu po prawej stronie
st.sidebar.title("Menu")
selected_page = st.sidebar.selectbox("Wybierz sekcję", ["Wprowadzenie", "Eksploracja danych", "Wizualizacja danych", "Analiza relacji"])  # Dodano "Analiza relacji"

# Wyświetlanie odpowiedniej sekcji na podstawie wyboru użytkownika
if selected_page == "Wprowadzenie":
    show_welcome()
elif selected_page == "Eksploracja danych":
    show_exploration()
elif selected_page == "Wizualizacja danych":
    show_visualization()
elif selected_page == "Analiza relacji":  
    show_relationship_analysis()
