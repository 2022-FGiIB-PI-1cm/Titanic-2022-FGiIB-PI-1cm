import streamlit as st;
import math;
def variant_number_2_banaev():
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
    with open("data.csv") as file:
        name = []
        age = []
        class_p = []
        for line in file:
            if line.split(',')[1] == save and line.split(',')[5] == sex_titanic:
                name_titanic = [line.split(',')[3] + line.split(',')[4]]
                name.append(name_titanic)
                age_titanic = [line.split(',')[6]]
                age.append(age_titanic)
                class_p_titanic = [line.split(',')[2]]
                class_p.append(class_p_titanic)
                titanic = {'Имя': name, 'Возраст': age, 'Класс билета': class_p}
    st.dataframe(titanic)

def variant_number_3_belinskiy ():
    #st.header("Лабораторная работа № 9, вариант № 3, Белинский В. А., группа № 2022-ФГиИБ-ПИ-1см");

    #st.subheader('Анализ данных пассажиров парохода "Титаник"');

    st.info(
        "Для вывода имён, возрастов, классов билетов мужчин указанного возраста (от 30 до 60 лет) необходимо задать возрастной диапазон.")

    min_value_age = st.number_input("Введите минимальное значение возраста:", 30, 60, 30, 1, key=0);
    min_value_age = float(min_value_age);
    max_value_age = st.number_input("Введите максимальное значение возраста:", 30, 60, 60, 1, key=1);
    max_value_age = float(max_value_age);

    # C:\Users\Cybernetics\PycharmProjects\Лабораторные_работы\laboratory_work_9\data.csv - этот абсолютный путь необходимо заменить на свой
    # для корректной работы элементов streamlit в разных браузерах!

    if (st.button("Найти")):
        with open("data.csv") as file:
            next(file);
            for row in file:
                min_value_age = min_value_age;
                max_value_age = max_value_age;
                age = row.rstrip().split(',')[6];
                male = row.rstrip().split(',')[5];
                for i in age:
                    if i == "":
                        age.remove(i);
                    age = float(age);
                    age = math.floor(age);
                    print(min_value_age);
                    if age >= min_value_age and age <= max_value_age and male == 'male':
                        st.text(row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' +
                                row.rstrip().split(',')[
                                    6] + ' - ' + row.rstrip().split(',')[2]);
                    break;

st.header("Лабораторная работа № 10, группа № 2022-ФГиИБ-ПИ-1см");

st.subheader('Анализ данных пассажиров парохода "Титаник"');

variants = st.radio("Выберите интересующий вариант анализа из предложенных в списке:", ('Вариант № 2 - Банаев Ю. А.','Вариант № 3 - Белинский В. А.'))

if variants == 'Вариант № 2 - Банаев Ю. А.':
    variant_number_2_banaev();
if variants == 'Вариант № 3 - Белинский В. А.':
    variant_number_3_belinskiy();