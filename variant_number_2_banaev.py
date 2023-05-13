# Юрий Банаев группа 2022-ФГиИБ-ПИ-1см
# Вариант № 2


with open("data.csv") as file:
    data = file.readlines();


def get_pass_list(data, save, sex):
    out_list = []
    for line in data:
        if line.split(',')[1] == save and line.split(',')[5] == sex:
            out_list += [line]
    return out_list