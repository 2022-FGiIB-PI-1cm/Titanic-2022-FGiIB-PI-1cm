# Тесты Банаева Ю. А. 
from variant_number_2_banaev import get_pass_list


def test_pass_list_one1():
    data = ['0,1,2,3,4,female,1', '1,0,2,3,4,male,1', '2,1,2,3,4,male,1']
    assert get_pass_list(data, '1', 'male') == {'Возраст': [['1']], 'Имя': [['34']], 'Класс билета': [['2']]}


def test_pass_list_one2():
    data = ['0,1,2,3,4,female,1', '1,0,2,3,4,male,1', '2,1,2,3,4,male,3']
    assert get_pass_list(data, '1', 'male') == {'Возраст': [['3']], 'Имя': [['34']], 'Класс билета': [['2']]}
