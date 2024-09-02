import matplotlib.pyplot as plt
import streamlit as st

def plot_animals_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        dog_data = data[data['Ulubione zwierzęta'] == 'Psy'][column].value_counts().reindex(categories_order, fill_value=0)
        others_data = data[data['Ulubione zwierzęta'] == 'Inne'][column].value_counts().reindex(categories_order, fill_value=0)
        cat_data = data[data['Ulubione zwierzęta'] == 'Koty'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_data = data[data['Ulubione zwierzęta'] == 'Brak ulubionych'][column].value_counts().reindex(categories_order, fill_value=0)
        dogcat_data = data[data['Ulubione zwierzęta'] == 'Koty i Psy'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        dog_data = data[data['Ulubione zwierzęta'] == 'Psy'][column].value_counts().reindex(common_categories, fill_value=0)
        others_data = data[data['Ulubione zwierzęta'] == 'Inne'][column].value_counts().reindex(common_categories, fill_value=0)
        cat_data = data[data['Ulubione zwierzęta'] == 'Koty'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_data = data[data['Ulubione zwierzęta'] == 'Brak ulubionych'][column].value_counts().reindex(common_categories, fill_value=0)
        dogcat_data = data[data['Ulubione zwierzęta'] == 'Koty i Psy'][column].value_counts().reindex(common_categories, fill_value=0)

    total_data = dog_data + others_data + cat_data + brak_data + dogcat_data 

    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        dog_data = dog_data.reindex(total_data.index)
        others_data = others_data.reindex(total_data.index)
        cat_data = cat_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)
        dogcat_data = dogcat_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(dog_data.index, dog_data, label='Psy', color='blue')
        ax.bar(others_data.index, others_data, bottom=dog_data, label='Inne', color='orange')
        ax.bar(cat_data.index, cat_data, bottom=dog_data + others_data, label='Koty', color='green')
        ax.bar(brak_data.index, brak_data, bottom=dog_data + others_data + cat_data , label='Brak ulubionych', color='red')
        ax.bar(dogcat_data.index, dogcat_data, bottom=dog_data + others_data + cat_data + brak_data, label='Koty i Psy', color='purple')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(dog_data.index, dog_data, label='Psy', color='blue')
        ax.barh(others_data.index, others_data, left=dog_data, label='Inne', color='orange')
        ax.barh(cat_data.index, cat_data, left=dog_data + others_data, label='Koty', color='green')
        ax.barh(brak_data.index, brak_data, left=dog_data + others_data + cat_data, label='Brak ulubionych', color='red')
        ax.barh(dogcat_data.index, dogcat_data, left=dog_data + others_data + cat_data + brak_data, label='Koty i Psy', color='purple')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_places_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        water_data = data[data['Ulubione miejsce'] == 'Nad wodą'][column].value_counts().reindex(categories_order, fill_value=0)
        mountains_data = data[data['Ulubione miejsce'] == 'W górach'][column].value_counts().reindex(categories_order, fill_value=0)
        forest_data = data[data['Ulubione miejsce'] == 'W lesie'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_data = data[data['Ulubione miejsce'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
        inne_data = data[data['Ulubione miejsce'] == 'Inne'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        water_data = data[data['Ulubione miejsce'] == 'Nad wodą'][column].value_counts().reindex(common_categories, fill_value=0)
        mountains_data = data[data['Ulubione miejsce'] == 'W górach'][column].value_counts().reindex(common_categories, fill_value=0)
        forest_data = data[data['Ulubione miejsce'] == 'W lesie'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_data = data[data['Ulubione miejsce'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)
        inne_data = data[data['Ulubione miejsce'] == 'Inne'][column].value_counts().reindex(common_categories, fill_value=0)

    total_data = water_data + mountains_data + forest_data + brak_data + inne_data
    
    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        water_data = water_data.reindex(total_data.index)
        mountains_data = mountains_data.reindex(total_data.index)
        forest_data = forest_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)
        inne_data = inne_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(water_data.index, water_data, label='Nad wodą', color='blue')
        ax.bar(mountains_data.index, mountains_data, bottom=water_data, label='W górach', color='orange')
        ax.bar(forest_data.index, forest_data, bottom=water_data + mountains_data, label='W lesie', color='green')
        ax.bar(brak_data.index, brak_data, bottom=water_data + mountains_data + forest_data, label='Brak danych', color='black')
        ax.bar(inne_data.index, inne_data, bottom=water_data + mountains_data + forest_data + brak_data, label='Inne', color='purple')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(water_data.index, water_data, label='Nad wodą', color='blue')
        ax.barh(mountains_data.index, mountains_data, left=water_data, label='W górach', color='orange')
        ax.barh(forest_data.index, forest_data, left=water_data + mountains_data, label='W lesie', color='green')
        ax.barh(brak_data.index, brak_data, left=water_data + mountains_data + forest_data, label='Brak danych', color='black')
        ax.barh(inne_data.index, inne_data, left=water_data + mountains_data + forest_data + brak_data, label='Inne', color='purple')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_sweet_salty_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        sweet_data = data[data['Słodki czy słony'] == 'Słodki'][column].value_counts().reindex(categories_order, fill_value=0)
        salty_data = data[data['Słodki czy słony'] == 'Słony'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_data = data[data['Słodki czy słony'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        sweet_data = data[data['Słodki czy słony'] == 'Słodki'][column].value_counts().reindex(common_categories, fill_value=0)
        salty_data = data[data['Słodki czy słony'] == 'Słony'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_data = data[data['Słodki czy słony'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)

    total_data = sweet_data + salty_data + brak_data

    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        sweet_data = sweet_data.reindex(total_data.index)
        salty_data = salty_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(sweet_data.index, sweet_data, label='Słodki', color='blue')
        ax.bar(salty_data.index, salty_data, bottom=sweet_data, label='Słony', color='orange')
        ax.bar(brak_data.index, brak_data, bottom=sweet_data + salty_data, label='Brak danych', color='black')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(sweet_data.index, sweet_data, label='Słodki', color='blue')
        ax.barh(salty_data.index, salty_data, left=sweet_data, label='Słony', color='orange')
        ax.barh(brak_data.index, brak_data, left=sweet_data + salty_data, label='Brak danych', color='black')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_grouped_bar_chart_3(data, columns, title, prefix):
    fig, ax = plt.subplots(figsize=(14, 10))
    if st.session_state['split_by_animals']:
        dog_data = data[data['Ulubione zwierzęta'] == 'Psy'][columns].sum()
        others_data = data[data['Ulubione zwierzęta'] == 'Inne'][columns].sum()
        cat_data = data[data['Ulubione zwierzęta'] == 'Koty'][columns].sum()
        brak_data = data[data['Ulubione zwierzęta'] == 'Brak ulubionych'][columns].sum()
        dogcat_data = data[data['Ulubione zwierzęta'] == 'Koty i Psy'][columns].sum()

        dog_data.index = dog_data.index.str.replace(prefix, '')
        others_data.index = others_data.index.str.replace(prefix, '')
        cat_data.index = cat_data.index.str.replace(prefix, '')
        brak_data.index = brak_data.index.str.replace(prefix, '')
        dogcat_data.index = dogcat_data.index.str.replace(prefix, '')

        total_data = (dog_data + others_data + cat_data + brak_data + dogcat_data)
                   
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        dog_data = dog_data.reindex(total_data.index)
        cat_data = cat_data.reindex(total_data.index)
        others_data = others_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)
        dogcat_data = dogcat_data.reindex(total_data.index)

        ax.barh(dog_data.index, dog_data, label='Psy', color='blue')
        ax.barh(others_data.index, others_data, left=dog_data, label='Inne', color='orange')
        ax.barh(cat_data.index, cat_data, left=dog_data + others_data, label='Koty', color='green')
        ax.barh(brak_data.index, brak_data, left=dog_data + others_data + cat_data, label='Brak ulubionych', color='black')
        ax.barh(dogcat_data.index, dogcat_data, left=dog_data + others_data + cat_data + brak_data, label='Koty i Psy', color='purple')

    elif st.session_state['split_by_places']:
        water_data = data[data['Ulubione miejsce'] == 'Nad wodą'][columns].sum()
        mountains_data = data[data['Ulubione miejsce'] == 'W górach'][columns].sum()
        forest_data = data[data['Ulubione miejsce'] == 'W lesie'][columns].sum()
        brak_data = data[data['Ulubione miejsce'] == 'Brak danych'][columns].sum()
        inne_data = data[data['Ulubione miejsce'] == 'Inne'][columns].sum()

        water_data.index = water_data.index.str.replace(prefix, '')
        mountains_data.index = mountains_data.index.str.replace(prefix, '')
        forest_data.index = forest_data.index.str.replace(prefix, '')
        brak_data.index = brak_data.index.str.replace(prefix, '')
        inne_data.index = inne_data.index.str.replace(prefix, '')

        total_data = (water_data + mountains_data + forest_data + brak_data + inne_data)
        
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        water_data = water_data.reindex(total_data.index)
        mountains_data = mountains_data.reindex(total_data.index)
        forest_data = forest_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)
        inne_data = inne_data.reindex(total_data.index)

        ax.barh(water_data.index, water_data, label='Nad wodą', color='blue')
        ax.barh(mountains_data.index, mountains_data, left=water_data, label='W górach', color='orange')
        ax.barh(forest_data.index, forest_data, left=water_data + mountains_data, label='W lesie', color='green')
        ax.barh(brak_data.index, brak_data, left=water_data + mountains_data + forest_data, label='Brak danych', color='black')
        ax.barh(inne_data.index, inne_data, left=water_data + mountains_data + forest_data, label='Inne', color='purple')

    elif st.session_state['split_by_sweet_salty']:
        sweet_data = data[data['Słodki czy słony'] == 'Słodki'][columns].sum()
        salty_data = data[data['Słodki czy słony'] == 'Słony'][columns].sum()
        brak_data = data[data['Słodki czy słony'] == 'Brak danych'][columns].sum()

        sweet_data.index = sweet_data.index.str.replace(prefix, '')
        salty_data.index = salty_data.index.str.replace(prefix, '')
        brak_data.index = brak_data.index.str.replace(prefix, '')

        total_data = (sweet_data + salty_data + brak_data)
        
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        sweet_data = sweet_data.reindex(total_data.index)
        salty_data = salty_data.reindex(total_data.index)
        brak_data = brak_data.reindex(total_data.index)

        ax.barh(sweet_data.index, sweet_data, label='Słodki', color='blue')
        ax.barh(salty_data.index, salty_data, left=sweet_data, label='Słony', color='orange')
        ax.barh(brak_data.index, brak_data, left=sweet_data + salty_data, label='Brak danych', color='black')

    else:
        total_data = data[columns].sum()
        total_data.index = total_data.index.str.replace(prefix, '')
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        ax.barh(total_data.index, total_data, color='blue')

    ax.set_title(title, fontsize=18)
    ax.set_xlabel('Liczba', fontsize=14)
    ax.set_ylabel('Kategorie', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)
