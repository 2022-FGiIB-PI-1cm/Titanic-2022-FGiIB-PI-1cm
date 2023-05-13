#Лабораторная работа № 12, вариант № 3, Белинский В. А., группа № 2022-ФГиИБ-ПИ-1см

import  math;

with open("data.csv") as file:
    next(file);
    for row in file:
        rows_data = file.readlines();
def getting_list_mens(rows_data, min_value_age, max_value_age, gender_person):
    result_rows = [];
    for row in rows_data:
        rows = row.rstrip().split(",");
        min_value_age = float (min_value_age);
        max_value_age = float (max_value_age);
        age = row.rstrip().split(',')[6];
        for i in age:
            if i == "":
                age.remove(i);
            age = float(age);
            age = math.floor(age);
            if age>=min_value_age and age<=max_value_age and rows[5]==gender_person:
                result_rows += [rows[3] + ' ' + rows[4] + ', ' + rows[6] + ', ' + rows[2]];
                break;
    return result_rows;