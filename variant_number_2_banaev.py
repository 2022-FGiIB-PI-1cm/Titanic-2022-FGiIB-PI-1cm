# Вячеслав Белинский группа 2022-ФГиИБ-ПИ-1см
# Вариант № 3

import streamlit as st

with open("data.csv") as file:
    next(file);
    for row in file:
        rows_data = file.readlines();

def getting_a_list_of_mens(rows_data, min_value_age, max_value_age, gender_of_the_person):
    if (st.button("Найти")):
     for row in rows_data:
        if row.split(',')[6]>=min_value_age and row.split(',')[6]<=max_value_age and row.split(',')[5]==gender_of_the_person:
            st.text (row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' + row.rstrip().split(',')[
            6] + ' - ' + row.rstrip().split(',')[2]);
