# Юрий Банаев группа 2022-ФГиИБ-ПИ-1см
# Вариант № 2

with open("data.csv") as file:
    data = file.readlines()

def get_pass_list(data, save, sex):
    name = []
    age = []
    class_p = []
    out_list = []
    for line in data:
        if line.split(',')[1] == save and line.split(',')[5] == sex:
            name_titanic = [line.split(',')[3] + line.split(',')[4]]
            name.append(name_titanic)
            age_titanic = [line.split(',')[6]]
            age.append(age_titanic)
            class_p_titanic = [line.split(',')[2]]
            class_p.append(class_p_titanic)
            out_list = {'Имя': name, 'Возраст': age, 'Класс билета': class_p}
    return out_list
