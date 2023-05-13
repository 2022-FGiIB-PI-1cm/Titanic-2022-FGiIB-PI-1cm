#Лабораторная работа № 12, вариант № 3, Белинский В. А., группа № 2022-ФГиИБ-ПИ-1см

#Тесты

from main import *

def test_getting_list_mens_1 ():
    rows_data = ['1,0,2,"Kirkland, Rev. Charles Leonard",male,57',
                 '2,0,1,"Kent, Mr. Edward Austin",male,58',
                 '3,0,1,"Newell, Mr. Arthur Webster",male,58'];

    assert getting_list_mens (rows_data,'57','58','male') == ['"Kirkland  Rev. Charles Leonard", 57, 2',
                                                              '"Kent  Mr. Edward Austin", 58, 1',
                                                              '"Newell  Mr. Arthur Webster", 58, 1'];

def test_getting_list_mens_2 ():
    rows_data = ['1,1,1,"Frolicher-Stehli, Mr. Maxmillian",male,60',
                 '2,0,2,"Brown, Mr. Thomas William Solomon",male,60',
                 '3,0,1,"Weir, Col. John",male,60'];

    assert getting_list_mens (rows_data,'60','60','male') == ['"Frolicher-Stehli  Mr. Maxmillian", 60, 1',
                                                              '"Brown  Mr. Thomas William Solomon", 60, 2',
                                                              '"Weir  Col. John", 60, 1'];

def test_getting_list_mens_3 ():
    rows_data = ['1,1,1,"Frolicher-Stehli, Mr. Maxmillian",male,60',
                 '2,0,2,"Brown, Mr. Thomas William Solomon",male,60',
                 '3,0,1,"Weir, Col. John",male,60'];

    assert getting_list_mens (rows_data,'60','60','female') == [];

