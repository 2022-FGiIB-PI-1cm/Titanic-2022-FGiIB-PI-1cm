# Юрий Банаев группа 2022-ФГиИБ-ПИ-1см
# Вариант № 2

import streamlit as st

st.title('Пассажиры Титаника')
if st.checkbox("Спасен?"):
    save = '1'
else:
    save = '0'
sex = st.radio("Пол:", ('Мужчина', 'Женщина'))
if (sex == 'Мужчина'):
    sex_titanic = 'male'
else:
    sex_titanic = 'female'
with open(r"C:\Users\Cybernetics\PycharmProjects\Лабораторные_работы\laboratory_work_9\data.csv") as file:
    name = []
    age=[]
    class_p = []
    for line in file:
        if line.split(',')[1] == save and line.split(',')[5] == sex_titanic:
            name_titanic = [line.split(',')[3] + line.split(',')[4]]
            name.append(name_titanic)
            age_titanic = [line.split(',')[6]]
            age.append(age_titanic)
            class_p_titanic = [line.split(',')[2]]
            class_p.append(class_p_titanic)
            titanic = {'Имя':name,'Возраст':age,'Класс билета':class_p}
st.dataframe(titanic)