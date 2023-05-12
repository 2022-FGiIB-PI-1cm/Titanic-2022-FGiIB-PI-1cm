#Тесты Белинского В. А.
from main import *
import os;
def test_getting_a_list_of_mens_number_1 ():
    assert os.path.isfile (r"C:\Users\Cybernetics\PycharmProjects\Лабораторные_работы\laboratory_work_12\data.csv") == True;

def test_getting_a_list_of_mens_number_2 ():
    assert rows_data !=0;

def test_getting_a_list_of_mens_number_3 ():
    min_value_age = st.number_input("Введите минимальное значение возраста:", 30, 60, 30, 1, key=0);
    min_value_age = str(min_value_age);
    max_value_age = st.number_input("Введите максимальное значение возраста:", 30, 60, 60, 1, key=1);
    max_value_age = str(max_value_age);
    gender_of_the_person = 'male';
    assert isinstance (rows_data, list) == True;
    assert isinstance (min_value_age, str) == True;
    assert isinstance (max_value_age, str) == True;
    assert isinstance (gender_of_the_person, str) == True;

def test_getting_a_list_of_mens_number_4 ():
    min_value_age = st.number_input("Введите минимальное значение возраста:", 30, 60, 30, 1, key=0);
    min_value_age = str(min_value_age);
    max_value_age = st.number_input("Введите максимальное значение возраста:", 30, 60, 60, 1, key=1);
    max_value_age = str(max_value_age);
    gender_of_the_person = 'male';
    assert getting_a_list_of_mens(rows_data, min_value_age, max_value_age, gender_of_the_person) != 0;

def test_getting_a_list_of_mens_number_5 ():
    result = [];
    for row in rows_data:
        if row.split(',')[6] >= '47' and row.split(',')[6] <= '48' and row.split(',')[5] == 'male':
            result.append(row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' + row.rstrip().split(',')[6] + ' - ' + row.rstrip().split(',')[2]);
    assert result == ['"Porter -  Mr. Walter Chamberlain" - 47 - 1',
                      '"Anderson -  Mr. Harry" - 48 - 1',
                      '"Gee -  Mr. Arthur H" - 47 - 1',
                      '"Milling -  Mr. Jacob Christian" - 48 - 2',
                      '"Walker -  Mr. William Anderson" - 47 - 1',
                      '"Jarvis -  Mr. John Denzil" - 47 - 2',
                      '"Elsbury -  Mr. William James" - 47 - 3',
                      '"Harper -  Mr. Henry Sleeper" - 48 - 1',
                      '"Colley -  Mr. Edward Pomeroy" - 47 - 1',
                      '"Taylor -  Mr. Elmer Zebley" - 48 - 1',
                      '"Jensen -  Mr. Niels Peder" - 48 - 3',
                      '"Vander Cruyssen -  Mr. Victor" - 47 - 3'];

def test_getting_a_list_of_mens_number_6 ():
    result = [];
    for row in rows_data:
        if row.split(',')[6] >= '57' and row.split(',')[6] <= '58' and row.split(',')[5] == 'male':
            result.append(row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' + row.rstrip().split(',')[6] + ' - ' + row.rstrip().split(',')[2]);
    assert result == ['"Kent -  Mr. Edward Austin" - 58 - 1', '"Kirkland -  Rev. Charles Leonard" - 57 - 2', '"Newell -  Mr. Arthur Webster" - 58 - 1'];

def test_getting_a_list_of_mens_number_7 ():
    result = [];
    for row in rows_data:
        if row.split(',')[6] >= '60' and row.split(',')[6] <= '60' and row.split(',')[5] == 'male':
            result.append(row.rstrip().split(',')[3] + ' - ' + row.rstrip().split(',')[4] + ' - ' + row.rstrip().split(',')[6] + ' - ' + row.rstrip().split(',')[2]);
    assert result == ['"Frolicher-Stehli -  Mr. Maxmillian" - 60 - 1', '"Brown -  Mr. Thomas William Solomon" - 60 - 2', '"Weir -  Col. John" - 60 - 1'];

