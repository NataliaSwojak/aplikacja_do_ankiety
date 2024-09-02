import matplotlib.pyplot as plt
import streamlit as st

def plot_branch_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        it_data = data[data['Branża'] == 'IT'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_danych_data = data[data['Branża'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
        finanse_data = data[data['Branża'] == 'Finanse'][column].value_counts().reindex(categories_order, fill_value=0)
        zdrowie_data = data[data['Branża'] == 'Zdrowie'][column].value_counts().reindex(categories_order, fill_value=0)
        edukacja_data = data[data['Branża'] == 'Edukacja'][column].value_counts().reindex(categories_order, fill_value=0)
        uslugi_data = data[data['Branża'] == 'Usługi'][column].value_counts().reindex(categories_order, fill_value=0)
        logistyka_data = data[data['Branża'] == 'Logistyka'][column].value_counts().reindex(categories_order, fill_value=0)
        energetyka_data = data[data['Branża'] == 'Energetyka'][column].value_counts().reindex(categories_order, fill_value=0)
        automotiv_data = data[data['Branża'] == 'Automotive'][column].value_counts().reindex(categories_order, fill_value=0)
        marketing_data = data[data['Branża'] == 'Marketing'][column].value_counts().reindex(categories_order, fill_value=0)
        pozostale_data = data[~data['Branża'].isin([
            'IT', 'Brak danych', 'Finanse', 'Zdrowie', 'Edukacja', 
            'Usługi', 'Logistyka', 'Energetyka', 'Automotive', 'Marketing'
        ])][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        it_data = data[data['Branża'] == 'IT'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_danych_data = data[data['Branża'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)
        finanse_data = data[data['Branża'] == 'Finanse'][column].value_counts().reindex(common_categories, fill_value=0)
        zdrowie_data = data[data['Branża'] == 'Zdrowie'][column].value_counts().reindex(common_categories, fill_value=0)
        edukacja_data = data[data['Branża'] == 'Edukacja'][column].value_counts().reindex(common_categories, fill_value=0)
        uslugi_data = data[data['Branża'] == 'Usługi'][column].value_counts().reindex(common_categories, fill_value=0)
        logistyka_data = data[data['Branża'] == 'Logistyka'][column].value_counts().reindex(common_categories, fill_value=0)
        energetyka_data = data[data['Branża'] == 'Energetyka'][column].value_counts().reindex(common_categories, fill_value=0)
        automotiv_data = data[data['Branża'] == 'Automotive'][column].value_counts().reindex(common_categories, fill_value=0)
        marketing_data = data[data['Branża'] == 'Marketing'][column].value_counts().reindex(common_categories, fill_value=0)
        pozostale_data = data[~data['Branża'].isin([
            'IT', 'Brak danych', 'Finanse', 'Zdrowie', 'Edukacja', 
            'Usługi', 'Logistyka', 'Energetyka', 'Automotive', 'Marketing'
        ])][column].value_counts().reindex(common_categories, fill_value=0)

    total_data = it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + \
                 uslugi_data + logistyka_data + energetyka_data + automotiv_data + \
                 marketing_data + pozostale_data

    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        it_data = it_data.reindex(total_data.index)
        brak_danych_data = brak_danych_data.reindex(total_data.index)
        finanse_data = finanse_data.reindex(total_data.index)
        zdrowie_data = zdrowie_data.reindex(total_data.index)
        edukacja_data = edukacja_data.reindex(total_data.index)
        uslugi_data = uslugi_data.reindex(total_data.index)
        logistyka_data = logistyka_data.reindex(total_data.index)
        energetyka_data = energetyka_data.reindex(total_data.index)
        automotiv_data = automotiv_data.reindex(total_data.index)
        marketing_data = marketing_data.reindex(total_data.index)
        pozostale_data = pozostale_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(it_data.index, it_data, label='IT', color='blue')
        ax.bar(brak_danych_data.index, brak_danych_data, bottom=it_data, label='Brak danych', color='black')
        ax.bar(finanse_data.index, finanse_data, bottom=it_data + brak_danych_data, label='Finanse', color='green')
        ax.bar(zdrowie_data.index, zdrowie_data, bottom=it_data + brak_danych_data + finanse_data, label='Zdrowie', color='red')
        ax.bar(edukacja_data.index, edukacja_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data, label='Edukacja', color='purple')
        ax.bar(uslugi_data.index, uslugi_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data, label='Usługi', color='brown')
        ax.bar(logistyka_data.index, logistyka_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data, label='Logistyka', color='pink')
        ax.bar(energetyka_data.index, energetyka_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data, label='Energetyka', color='gray')
        ax.bar(automotiv_data.index, automotiv_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data, label='Automotive', color='cyan')
        ax.bar(marketing_data.index, marketing_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data, label='Marketing', color='yellow')
        ax.bar(pozostale_data.index, pozostale_data, bottom=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data + marketing_data, label='Pozostałe', color='orange')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(it_data.index, it_data, label='IT', color='blue')
        ax.barh(brak_danych_data.index, brak_danych_data, left=it_data, label='Brak danych', color='black')
        ax.barh(finanse_data.index, finanse_data, left=it_data + brak_danych_data, label='Finanse', color='green')
        ax.barh(zdrowie_data.index, zdrowie_data, left=it_data + brak_danych_data + finanse_data, label='Zdrowie', color='red')
        ax.barh(edukacja_data.index, edukacja_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data, label='Edukacja', color='purple')
        ax.barh(uslugi_data.index, uslugi_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data, label='Usługi', color='brown')
        ax.barh(logistyka_data.index, logistyka_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data, label='Logistyka', color='pink')
        ax.barh(energetyka_data.index, energetyka_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data, label='Energetyka', color='gray')
        ax.barh(automotiv_data.index, automotiv_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data, label='Automotiv', color='cyan')
        ax.barh(marketing_data.index, marketing_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data, label='Marketing', color='yellow')
        ax.barh(pozostale_data.index, pozostale_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data + marketing_data, label='Pozostałe', color='orange')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_experience_split_bar_chart(data, column, title, categories_order=None, sort_data=True, is_vertical=False):
    fig, ax = plt.subplots(figsize=(14, 10))
    if categories_order:
        experience_0_2_data = data[data['Lata doświadczenia'] == '0-2'][column].value_counts().reindex(categories_order, fill_value=0)
        experience_3_5_data = data[data['Lata doświadczenia'] == '3-5'][column].value_counts().reindex(categories_order, fill_value=0)
        experience_6_10_data = data[data['Lata doświadczenia'] == '6-10'][column].value_counts().reindex(categories_order, fill_value=0)
        experience_11_15_data = data[data['Lata doświadczenia'] == '11-15'][column].value_counts().reindex(categories_order, fill_value=0)
        experience_16_plus_data = data[data['Lata doświadczenia'] == '>=16'][column].value_counts().reindex(categories_order, fill_value=0)
        brak_danych_data = data[data['Lata doświadczenia'] == 'Brak danych'][column].value_counts().reindex(categories_order, fill_value=0)
    else:
        common_categories = data[column].value_counts().index
        experience_0_2_data = data[data['Lata doświadczenia'] == '0-2'][column].value_counts().reindex(common_categories, fill_value=0)
        experience_3_5_data = data[data['Lata doświadczenia'] == '3-5'][column].value_counts().reindex(common_categories, fill_value=0)
        experience_6_10_data = data[data['Lata doświadczenia'] == '6-10'][column].value_counts().reindex(common_categories, fill_value=0)
        experience_11_15_data = data[data['Lata doświadczenia'] == '11-15'][column].value_counts().reindex(common_categories, fill_value=0)
        experience_16_plus_data = data[data['Lata doświadczenia'] == '>=16'][column].value_counts().reindex(common_categories, fill_value=0)
        brak_danych_data = data[data['Lata doświadczenia'] == 'Brak danych'][column].value_counts().reindex(common_categories, fill_value=0)

    total_data = experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data + experience_16_plus_data + brak_danych_data
    if total_data.sum() == 0:
        return
    if sort_data:
        total_data = total_data.sort_values(ascending=True)
        experience_0_2_data = experience_0_2_data.reindex(total_data.index)
        experience_3_5_data = experience_3_5_data.reindex(total_data.index)
        experience_6_10_data = experience_6_10_data.reindex(total_data.index)
        experience_11_15_data = experience_11_15_data.reindex(total_data.index)
        experience_16_plus_data = experience_16_plus_data.reindex(total_data.index)
        brak_danych_data = brak_danych_data.reindex(total_data.index)

    if is_vertical:
        ax.bar(experience_0_2_data.index, experience_0_2_data, label='0-2', color='blue')
        ax.bar(experience_3_5_data.index, experience_3_5_data, bottom=experience_0_2_data, label='3-5', color='orange')
        ax.bar(experience_6_10_data.index, experience_6_10_data, bottom=experience_0_2_data + experience_3_5_data, label='6-10', color='green')
        ax.bar(experience_11_15_data.index, experience_11_15_data, bottom=experience_0_2_data + experience_3_5_data + experience_6_10_data, label='11-15', color='red')
        ax.bar(experience_16_plus_data.index, experience_16_plus_data, bottom=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data, label='>=16', color='purple')
        ax.bar(brak_danych_data.index, brak_danych_data, bottom=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data + experience_16_plus_data, label='Brak danych', color='black')
        ax.set_ylabel('Liczba', fontsize=14)
        ax.set_xlabel(column, fontsize=14)
        plt.xticks(rotation=0, fontsize=12)
    else:
        ax.barh(experience_0_2_data.index, experience_0_2_data, label='0-2', color='blue')
        ax.barh(experience_3_5_data.index, experience_3_5_data, left=experience_0_2_data, label='3-5', color='orange')
        ax.barh(experience_6_10_data.index, experience_6_10_data, left=experience_0_2_data + experience_3_5_data, label='6-10', color='green')
        ax.barh(experience_11_15_data.index, experience_11_15_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data, label='11-15', color='red')
        ax.barh(experience_16_plus_data.index, experience_16_plus_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data, label='>=16', color='purple')
        ax.barh(brak_danych_data.index, brak_danych_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data + experience_16_plus_data, label='Brak danych', color='black')
        ax.set_xlabel('Liczba', fontsize=14)
        ax.set_ylabel(column, fontsize=14)

    ax.set_title(title, fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    ax.legend()
    st.pyplot(fig)

def plot_grouped_bar_chart_2(data, columns, title, prefix):
    fig, ax = plt.subplots(figsize=(14, 10))
    if st.session_state['split_by_branch']:
        it_data = data[data['Branża'] == 'IT'][columns].sum()
        brak_danych_data = data[data['Branża'] == 'Brak danych'][columns].sum()
        finanse_data = data[data['Branża'] == 'Finanse'][columns].sum()
        zdrowie_data = data[data['Branża'] == 'Zdrowie'][columns].sum()
        edukacja_data = data[data['Branża'] == 'Edukacja'][columns].sum()
        uslugi_data = data[data['Branża'] == 'Usługi'][columns].sum()
        logistyka_data = data[data['Branża'] == 'Logistyka'][columns].sum()
        energetyka_data = data[data['Branża'] == 'Energetyka'][columns].sum()
        automotiv_data = data[data['Branża'] == 'Automotive'][columns].sum()
        marketing_data = data[data['Branża'] == 'Marketing'][columns].sum()
        pozostale_data = data[~data['Branża'].isin([
            'IT', 'Finanse', 'Zdrowie', 'Edukacja', 'Usługi', 
            'Logistyka', 'Energetyka', 'Automotive', 'Marketing', 'Brak danych'
        ])][columns].sum()

        it_data.index = it_data.index.str.replace(prefix, '')
        brak_danych_data.index = brak_danych_data.index.str.replace(prefix, '')
        finanse_data.index = finanse_data.index.str.replace(prefix, '')
        zdrowie_data.index = zdrowie_data.index.str.replace(prefix, '')
        edukacja_data.index = edukacja_data.index.str.replace(prefix, '')
        uslugi_data.index = uslugi_data.index.str.replace(prefix, '')
        logistyka_data.index = logistyka_data.index.str.replace(prefix, '')
        energetyka_data.index = energetyka_data.index.str.replace(prefix, '')
        automotiv_data.index = automotiv_data.index.str.replace(prefix, '')
        marketing_data.index = marketing_data.index.str.replace(prefix, '')
        pozostale_data.index = pozostale_data.index.str.replace(prefix, '')

        total_data = (it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + 
                      uslugi_data + logistyka_data + energetyka_data + 
                      automotiv_data + marketing_data + pozostale_data)
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        it_data = it_data.reindex(total_data.index)
        brak_danych_data = brak_danych_data.reindex(total_data.index)
        finanse_data = finanse_data.reindex(total_data.index)
        zdrowie_data = zdrowie_data.reindex(total_data.index)
        edukacja_data = edukacja_data.reindex(total_data.index)
        uslugi_data = uslugi_data.reindex(total_data.index)
        logistyka_data = logistyka_data.reindex(total_data.index)
        energetyka_data = energetyka_data.reindex(total_data.index)
        automotiv_data = automotiv_data.reindex(total_data.index)
        marketing_data = marketing_data.reindex(total_data.index)
        pozostale_data = pozostale_data.reindex(total_data.index)

        ax.barh(it_data.index, it_data, label='IT', color='blue')
        ax.barh(brak_danych_data.index, brak_danych_data, left=it_data, label='Brak danych', color='black')
        ax.barh(finanse_data.index, finanse_data, left=it_data + brak_danych_data, label='Finanse', color='green')
        ax.barh(zdrowie_data.index, zdrowie_data, left=it_data + brak_danych_data + finanse_data, label='Zdrowie', color='red')
        ax.barh(edukacja_data.index, edukacja_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data, label='Edukacja', color='purple')
        ax.barh(uslugi_data.index, uslugi_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data, label='Usługi', color='brown')
        ax.barh(logistyka_data.index, logistyka_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data, label='Logistyka', color='pink')
        ax.barh(energetyka_data.index, energetyka_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data, label='Energetyka', color='gray')
        ax.barh(automotiv_data.index, automotiv_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data, label='Automotive', color='cyan')
        ax.barh(marketing_data.index, marketing_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data, label='Marketing', color='yellow')
        ax.barh(pozostale_data.index, pozostale_data, left=it_data + brak_danych_data + finanse_data + zdrowie_data + edukacja_data + uslugi_data + logistyka_data + energetyka_data + automotiv_data + marketing_data, label='Pozostałe', color='orange')

    elif st.session_state['split_by_experience']:
        experience_0_2_data = data[data['Lata doświadczenia'] == '0-2'][columns].sum()
        experience_3_5_data = data[data['Lata doświadczenia'] == '3-5'][columns].sum()
        experience_6_10_data = data[data['Lata doświadczenia'] == '6-10'][columns].sum()
        experience_11_15_data = data[data['Lata doświadczenia'] == '11-15'][columns].sum()
        experience_16_plus_data = data[data['Lata doświadczenia'] == '>=16'][columns].sum()
        brak_danych_data = data[data['Lata doświadczenia'] == 'Brak danych'][columns].sum()

        experience_0_2_data.index = experience_0_2_data.index.str.replace(prefix, '')
        experience_3_5_data.index = experience_3_5_data.index.str.replace(prefix, '')
        experience_6_10_data.index = experience_6_10_data.index.str.replace(prefix, '')
        experience_11_15_data.index = experience_11_15_data.index.str.replace(prefix, '')
        experience_16_plus_data.index = experience_16_plus_data.index.str.replace(prefix, '')
        brak_danych_data.index = brak_danych_data.index.str.replace(prefix, '')

        total_data = (experience_0_2_data + experience_3_5_data + experience_6_10_data + 
                      experience_11_15_data + experience_16_plus_data + brak_danych_data)
        if total_data.sum() == 0:
            return
        total_data = total_data.sort_values(ascending=True)
        experience_0_2_data = experience_0_2_data.reindex(total_data.index)
        experience_3_5_data = experience_3_5_data.reindex(total_data.index)
        experience_6_10_data = experience_6_10_data.reindex(total_data.index)
        experience_11_15_data = experience_11_15_data.reindex(total_data.index)
        experience_16_plus_data = experience_16_plus_data.reindex(total_data.index)
        brak_danych_data = brak_danych_data.reindex(total_data.index)

        ax.barh(experience_0_2_data.index, experience_0_2_data, label='0-2', color='blue')
        ax.barh(experience_3_5_data.index, experience_3_5_data, left=experience_0_2_data, label='3-5', color='orange')
        ax.barh(experience_6_10_data.index, experience_6_10_data, left=experience_0_2_data + experience_3_5_data, label='6-10', color='green')
        ax.barh(experience_11_15_data.index, experience_11_15_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data, label='11-15', color='red')
        ax.barh(experience_16_plus_data.index, experience_16_plus_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data, label='>=16', color='purple')
        ax.barh(brak_danych_data.index, brak_danych_data, left=experience_0_2_data + experience_3_5_data + experience_6_10_data + experience_11_15_data + experience_16_plus_data, label='Brak danych', color='black')

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
