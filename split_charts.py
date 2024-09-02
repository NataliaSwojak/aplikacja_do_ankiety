import matplotlib.pyplot as plt
import streamlit as st

def plot_gender_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        male_data = data[data['Płeć'] == 'Mężczyzna'][column].value_counts().reindex(categories_order, fill_value=0)
        female_data = data[data['Płeć'] == 'Kobieta'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_data = data[data['Płeć'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        male_data = data[data['Płeć'] == 'Mężczyzna'][column].value_counts().reindex(common_categories, fill_value=0)
        female_data = data[data['Płeć'] == 'Kobieta'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_data = data[data['Płeć'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)
    
    total_data = male_data + female_data + brak_data
    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        male_data = male_data.reindex(total_data.index)
        female_data = female_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(male_data.index, male_data, label='Mężczyźni', color='blue')
        ax.bar(female_data.index, female_data, bottom=male_data, label='Kobiety', color='orange')
        ax.bar(brak_data.index, brak_data, bottom=male_data + female_data, label='Brak danych', color='black')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(male_data.index, male_data, label='Mężczyźni', color='blue')
        ax.barh(female_data.index, female_data, left=male_data, label='Kobiety', color='orange')
        ax.barh(brak_data.index, brak_data, left=male_data + female_data, label='Brak danych', color='black')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_education_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        podstawowe_data = data[data['Poziom wykształcenia'] == 'Podstawowe'][column].value_counts().reindex(categories_order, fill_value=0)
        srednie_data = data[data['Poziom wykształcenia'] == 'Średnie'][column].value_counts().reindex(categories_order, fill_value=0)
        wyzsze_data = data[data['Poziom wykształcenia'] == 'Wyższe'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        podstawowe_data = data[data['Poziom wykształcenia'] == 'Podstawowe'][column].value_counts().reindex(common_categories, fill_value=0)
        srednie_data = data[data['Poziom wykształcenia'] == 'Średnie'][column].value_counts().reindex(common_categories, fill_value=0)
        wyzsze_data = data[data['Poziom wykształcenia'] == 'Wyższe'][column].value_counts().reindex(common_categories, fill_value=0)
    
    total_data = podstawowe_data + srednie_data + wyzsze_data
    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        podstawowe_data = podstawowe_data.reindex(total_data.index)
        srednie_data = srednie_data.reindex(total_data.index)
        wyzsze_data = wyzsze_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(wyzsze_data.index, wyzsze_data, label='Wyższe', color='blue')
        ax.bar(srednie_data.index, srednie_data, bottom=wyzsze_data, label='Średnie', color='orange')
        ax.bar(podstawowe_data.index, podstawowe_data, bottom=wyzsze_data + srednie_data, label='Podstawowe', color='green')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(wyzsze_data.index, wyzsze_data, label='Wyższe', color='blue')
        ax.barh(srednie_data.index, srednie_data, left=wyzsze_data, label='Średnie', color='orange')
        ax.barh(podstawowe_data.index, podstawowe_data, left=wyzsze_data + srednie_data, label='Podstawowe', color='green')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_age_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        age_under_18_data = data[data['Wiek'] == '<18'][column].value_counts().reindex(categories_order, fill_value=0)
        age_18_24_data = data[data['Wiek'] == '18-24'][column].value_counts().reindex(categories_order, fill_value=0)
        age_25_34_data = data[data['Wiek'] == '25-34'][column].value_counts().reindex(categories_order, fill_value=0)
        age_35_44_data = data[data['Wiek'] == '35-44'][column].value_counts().reindex(categories_order, fill_value=0)
        age_45_54_data = data[data['Wiek'] == '45-54'][column].value_counts().reindex(categories_order, fill_value=0)
        age_55_64_data = data[data['Wiek'] == '55-64'][column].value_counts().reindex(categories_order, fill_value=0)
        age_65_plus_data = data[data['Wiek'] == '>=65'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_data = data[data['Wiek'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        age_under_18_data = data[data['Wiek'] == '<18'][column].value_counts().reindex(common_categories, fill_value=0)
        age_18_24_data = data[data['Wiek'] == '18-24'][column].value_counts().reindex(common_categories, fill_value=0)
        age_25_34_data = data[data['Wiek'] == '25-34'][column].value_counts().reindex(common_categories, fill_value=0)
        age_35_44_data = data[data['Wiek'] == '35-44'][column].value_counts().reindex(common_categories, fill_value=0)
        age_45_54_data = data[data['Wiek'] == '45-54'][column].value_counts().reindex(common_categories, fill_value=0)
        age_55_64_data = data[data['Wiek'] == '55-64'][column].value_counts().reindex(common_categories, fill_value=0)
        age_65_plus_data = data[data['Wiek'] == '>=65'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_data = data[data['Wiek'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)
    
    total_data = (age_under_18_data + age_18_24_data + age_25_34_data + 
                  age_35_44_data + age_45_54_data + age_55_64_data + age_65_plus_data + brak_data)
    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        age_under_18_data = age_under_18_data.reindex(total_data.index)
        age_18_24_data = age_18_24_data.reindex(total_data.index)
        age_25_34_data = age_25_34_data.reindex(total_data.index)
        age_35_44_data = age_35_44_data.reindex(total_data.index)
        age_45_54_data = age_45_54_data.reindex(total_data.index)
        age_55_64_data = age_55_64_data.reindex(total_data.index)
        age_65_plus_data = age_65_plus_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(age_under_18_data.index, age_under_18_data, label='<18', color='purple')
        ax.bar(age_18_24_data.index, age_18_24_data, bottom=age_under_18_data, label='18-24', color='blue')
        ax.bar(age_25_34_data.index, age_25_34_data, bottom=age_under_18_data + age_18_24_data, label='25-34', color='orange')
        ax.bar(age_35_44_data.index, age_35_44_data, bottom=age_under_18_data + age_18_24_data + age_25_34_data, label='35-44', color='red')
        ax.bar(age_45_54_data.index, age_45_54_data, bottom=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data, label='45-54', color='green')
        ax.bar(age_55_64_data.index, age_55_64_data, bottom=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data, label='55-64', color='brown')
        ax.bar(age_65_plus_data.index, age_65_plus_data, bottom=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data, label='>=65', color='pink')
        ax.bar(brak_data.index, brak_data, bottom=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data + age_65_plus_data, label='Brak danych', color='black')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(age_under_18_data.index, age_under_18_data, label='<18', color='purple')
        ax.barh(age_18_24_data.index, age_18_24_data, left=age_under_18_data, label='18-24', color='blue')
        ax.barh(age_25_34_data.index, age_25_34_data, left=age_under_18_data + age_18_24_data, label='25-34', color='orange')
        ax.barh(age_35_44_data.index, age_35_44_data, left=age_under_18_data + age_18_24_data + age_25_34_data, label='35-44', color='red')
        ax.barh(age_45_54_data.index, age_45_54_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data, label='45-54', color='green')
        ax.barh(age_55_64_data.index, age_55_64_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data, label='55-64', color='brown')
        ax.barh(age_65_plus_data.index, age_65_plus_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data, label='>=65', color='pink')
        ax.barh(brak_data.index, age_65_plus_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data +  age_65_plus_data, label='Brak danych', color='black')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_grouped_bar_chart_1(data, columns, title, prefix):
    fig, ax = plt.subplots(figsize=(14, 10))
    if st.session_state['split_by_gender']:
        male_data = data[data['Płeć'] == 'Mężczyzna'][columns].sum()
        female_data = data[data['Płeć'] == 'Kobieta'][columns].sum()
        brak_data = data[data['Płeć'] == 'Brak danych'][columns].sum()

        male_data.index = male_data.index.str.replace(prefix, '')
        female_data.index = female_data.index.str.replace(prefix, '')
        brak_data.index = brak_data.index.str.replace(prefix, '')

        total_data = male_data + female_data + brak_data
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        male_data = male_data.reindex(total_data.index)
        female_data = female_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

        ax.barh(male_data.index, male_data, label='Mężczyźni', color='blue')
        ax.barh(female_data.index, female_data, left=male_data, label='Kobiety', color='orange')
        ax.barh(brak_data.index, brak_data, left=male_data + female_data, label='Brak danych', color='black')
    elif st.session_state['split_by_edukation']:
        podstawowe_data = data[data['Poziom wykształcenia'] == 'Podstawowe'][columns].sum()
        srednie_data = data[data['Poziom wykształcenia'] == 'Średnie'][columns].sum()
        wyzsze_data = data[data['Poziom wykształcenia'] == 'Wyższe'][columns].sum()

        podstawowe_data.index = podstawowe_data.index.str.replace(prefix, '')
        srednie_data.index = srednie_data.index.str.replace(prefix, '')
        wyzsze_data.index = wyzsze_data.index.str.replace(prefix, '')

        total_data = podstawowe_data + srednie_data + wyzsze_data
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        podstawowe_data = podstawowe_data.reindex(total_data.index)
        srednie_data = srednie_data.reindex(total_data.index)
        wyzsze_data = wyzsze_data.reindex(total_data.index)

        ax.barh(wyzsze_data.index, wyzsze_data, label='Wyższe', color='blue')
        ax.barh(srednie_data.index, srednie_data, left=wyzsze_data, label='Średnie', color='orange')
        ax.barh(podstawowe_data.index, podstawowe_data, left=wyzsze_data + srednie_data, label='Podstawowe', color='green')
    elif st.session_state['split_by_age']:
        age_under_18_data = data[data['Wiek'] == '<18'][columns].sum()
        age_18_24_data = data[data['Wiek'] == '18-24'][columns].sum()
        age_25_34_data = data[data['Wiek'] == '25-34'][columns].sum()
        age_35_44_data = data[data['Wiek'] == '35-44'][columns].sum()
        age_45_54_data = data[data['Wiek'] == '45-54'][columns].sum()
        age_55_64_data = data[data['Wiek'] == '55-64'][columns].sum()
        age_65_plus_data = data[data['Wiek'] == '>=65'][columns].sum()
        brak_data = data[data['Wiek'] == 'Brak danych'][columns].sum()

        age_under_18_data.index = age_under_18_data.index.str.replace(prefix, '')
        age_18_24_data.index = age_18_24_data.index.str.replace(prefix, '')
        age_25_34_data.index = age_25_34_data.index.str.replace(prefix, '')
        age_35_44_data.index = age_35_44_data.index.str.replace(prefix, '')
        age_45_54_data.index = age_45_54_data.index.str.replace(prefix, '')
        age_55_64_data.index = age_55_64_data.index.str.replace(prefix, '')
        age_65_plus_data.index = age_65_plus_data.index.str.replace(prefix, '')
        brak_data.index = brak_data.index.str.replace(prefix, '')

        total_data = (age_under_18_data + age_18_24_data + age_25_34_data + 
                      age_35_44_data + age_45_54_data + age_55_64_data + age_65_plus_data + brak_data)
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        age_under_18_data = age_under_18_data.reindex(total_data.index)
        age_18_24_data = age_18_24_data.reindex(total_data.index)
        age_25_34_data = age_25_34_data.reindex(total_data.index)
        age_35_44_data = age_35_44_data.reindex(total_data.index)
        age_45_54_data = age_45_54_data.reindex(total_data.index)
        age_55_64_data = age_55_64_data.reindex(total_data.index)
        age_65_plus_data = age_65_plus_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

        ax.barh(age_under_18_data.index, age_under_18_data, label='<18', color='purple')
        ax.barh(age_18_24_data.index, age_18_24_data, left=age_under_18_data, label='18-24', color='blue')
        ax.barh(age_25_34_data.index, age_25_34_data, left=age_under_18_data + age_18_24_data, label='25-34', color='orange')
        ax.barh(age_35_44_data.index, age_35_44_data, left=age_under_18_data + age_18_24_data + age_25_34_data, label='35-44', color='red')
        ax.barh(age_45_54_data.index, age_45_54_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data, label='45-54', color='green')
        ax.barh(age_55_64_data.index, age_55_64_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data, label='55-64', color='brown')
        ax.barh(age_65_plus_data.index, age_65_plus_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data, label='>=65', color='pink')
        ax.barh(brak_data.index, brak_data, left=age_under_18_data + age_18_24_data + age_25_34_data + age_35_44_data + age_45_54_data + age_55_64_data + age_65_plus_data, label='Brak danych', color='black')
    else:
        total_data = data[columns].sum()
        total_data.index = total_data.index.str.replace(prefix, '')
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)

        # Ręczne dodanie etykiet
        ax.barh(total_data.index, total_data, color='blue', label="Kategorie wyboru")

    ax.set_title(title, fontsize=18)
    ax.set_xlabel('Liczba', fontsize=14)
    ax.set_ylabel('Kategorie', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)