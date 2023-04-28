import streamlit as st;
import math;

st.header ("Лабораторная работа № 9, вариант № 3, Белинский В. А., группа № 2022-ФГиИБ-ПИ-1см");

st.subheader('Анализ данных пассажиров парохода "Титаник"');

st.info ("Для вывода имён, возрастов, классов билетов мужчин указанного возраста (от 30 до 60 лет) необходимо задать возрастной диапазон.")


min_value_age = st.number_input("Введите минимальное значение возраста:", 30, 60, 30, 1, key=0);
min_value_age = float(min_value_age);
max_value_age = st.number_input("Введите максимальное значение возраста:", 30, 60, 60, 1, key=1);
max_value_age = float(max_value_age);

#C:\Users\Cybernetics\PycharmProjects\Лабораторные_работы\laboratory_work_9\data.csv - этот абсолютный путь необходимо заменить на свой
# для корректной работы элементов streamlit в разных браузерах!

if(st.button("Найти")):
 with open (r"C:\Users\Cybernetics\PycharmProjects\Лабораторные_работы\laboratory_work_9\data.csv") as file:
    next(file);
    for row in file:
        min_value_age = min_value_age;
        max_value_age = max_value_age;
        age = row.rstrip().split(',')[6];
        male = row.rstrip().split(',')[5];
        for i in age:
            if i == "":
                age.remove(i);
            age = float (age);
            age = math.floor(age);
            print (min_value_age);
            if age>=min_value_age and age<=max_value_age and male=='male':
                st.text(row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' + row.rstrip().split(',')[
                   6] + ' - ' + row.rstrip().split(',')[2]);
            break;