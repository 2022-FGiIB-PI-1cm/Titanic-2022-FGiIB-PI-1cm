import streamlit as st;

from variant_number_2_banaev import get_pass_list,data
from variant_number_3_belinskiy import rows_data, getting_list_mens

st.header("Лабораторная работа № 12, группа № 2022-ФГиИБ-ПИ-1см");

st.subheader('Анализ данных пассажиров парохода "Титаник"');

variants = st.radio("Выберите интересующий вариант анализа из предложенных в списке:", ('Вариант № 2 - Банаев Ю. А.', 'Вариант № 3 - Белинский В. А.'))

if variants == 'Вариант № 2 - Банаев Ю. А.':
    sex = st.selectbox("Пол какой?", ['male', 'female'])
    save = st.selectbox("Спасен?", ['0', '1'])
    st.dataframe(get_pass_list(data, save, sex));

if variants == 'Вариант № 3 - Белинский В. А.':
    st.info("Для вывода имён, возрастов, классов билетов мужчин указанного возраста (от 30 до 60 лет) необходимо задать возрастной диапазон.");
    min_value_age = st.number_input("Введите минимальное значение возраста:", 30, 60, 30, 1, key=0);
    min_value_age = str(min_value_age);
    max_value_age = st.number_input("Введите максимальное значение возраста:", 30, 60, 60, 1, key=1);
    max_value_age = str(max_value_age);
    gender_person = 'male';
    if (st.button("Найти")):
        result_data = getting_list_mens(rows_data, min_value_age, max_value_age, gender_person);
        name_person = [];
        age_person = [];
        ticket_class = [];
        for row in result_data:
            rows = row.rstrip().split(",");
            name_person += [rows[0]];
            age_person += [rows[1]];
            ticket_class += [rows[2]];
            result_data = {'Ф. И. О.': name_person, 'Возраст': age_person, 'Класс билета': ticket_class};
        st.table(result_data);