# Тесты Банаева Ю. А.
from main import get_pass_list

def test_pass_list_all():
    data = ['0,1,2,3,4,male', '0,1,2,3,4,male', '0,1,2,3,4,male']
    assert get_pass_list(data, '1', 'male') == data


def test_pass_list_one():
   data = ['0,1,2,3,4,female', '1,0,2,3,4,male', '2,1,2,3,4,male']
   assert get_pass_list(data, '1', 'male') == ['2,1,2,3,4,male']
