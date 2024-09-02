import streamlit as st

def get_filters():
    
    if 'filters' not in st.session_state:
        st.session_state['filters'] = {
            'selected_plec': ["Wszystkie"],
            'selected_wiek': ["Wszystkie"],
            'selected_edukacja': ["Wszystkie"],
            'selected_branza': ["Wszystkie"],
            'selected_doswiadczenie': ["Wszystkie"],
            'selected_motywacja': ["Wszystkie"],
            'selected_nauka': ["Wszystkie"],
            'selected_hobby': ["Wszystkie"],
            'selected_zwierzeta': ["Wszystkie"],
            'selected_miejsce': ["Wszystkie"],
            'selected_slodki_sony': ["Wszystkie"],
        }
    return st.session_state['filters']

def update_filters(selected_plec, selected_wiek, selected_edukacja, selected_branza, selected_doswiadczenie,
                   selected_motywacja, selected_nauka, selected_hobby, selected_zwierzeta, selected_miejsce, selected_slodki_sony):
    
    st.session_state['filters'].update({
        'selected_plec': selected_plec,
        'selected_wiek': selected_wiek,
        'selected_edukacja': selected_edukacja,
        'selected_branza': selected_branza,
        'selected_doswiadczenie': selected_doswiadczenie,
        'selected_motywacja': selected_motywacja,
        'selected_nauka': selected_nauka,
        'selected_hobby': selected_hobby,
        'selected_zwierzeta': selected_zwierzeta,
        'selected_miejsce': selected_miejsce,
        'selected_slodki_sony': selected_slodki_sony,
    })

def reset_filters():
  
    st.session_state['filters'] = {
        'selected_plec': ["Wszystkie"],
        'selected_wiek': ["Wszystkie"],
        'selected_edukacja': ["Wszystkie"],
        'selected_branza': ["Wszystkie"],
        'selected_doswiadczenie': ["Wszystkie"],
        'selected_motywacja': ["Wszystkie"],
        'selected_nauka': ["Wszystkie"],
        'selected_hobby': ["Wszystkie"],
        'selected_zwierzeta': ["Wszystkie"],
        'selected_miejsce': ["Wszystkie"],
        'selected_slodki_sony': ["Wszystkie"],
    }
    st.rerun()
