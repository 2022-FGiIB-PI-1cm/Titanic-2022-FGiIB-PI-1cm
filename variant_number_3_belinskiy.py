#Лабораторная работа № 12, вариант № 3, Белинский В. А., группа № 2022-ФГиИБ-ПИ-1см


with open("data.csv") as file:
    next(file);
    for row in file:
        rows_data = file.readlines();
def getting_list_mens(rows_data, min_value_age, max_value_age, gender_person):
    result_rows = [];
    for row in rows_data:
        rows = row.rstrip().split(",");
        if rows[6]>=min_value_age and rows[6]<=max_value_age and rows[5]==gender_person:
            result_rows += [rows[3] + ' ' + rows[4] + ', ' + rows[6] + ', ' + rows[2]];
    return result_rows;