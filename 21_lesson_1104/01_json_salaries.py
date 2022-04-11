import json

with open('salaries.json') as json_file:
    content = json.loads(json_file.read())
    # читаю и преобразовываю файл в словарь Python
    print(type(content))
    for key in content:  # перебираю ключи из словаря
        salary = content[key]['fee']
        rate = content[key]['dollar_rate']
        sal_dol = salary / rate
        print(f'Год: {key}\nСредняя зарплата: {salary} руб.\nКурс $: {rate} руб.\nЗ/п в $: {sal_dol}')


