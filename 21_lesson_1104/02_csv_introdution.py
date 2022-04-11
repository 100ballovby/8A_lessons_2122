import csv


persons = [
    {'name': 'John Doe',
     'department': 'IT',
     'birthday': 'August'},
    {'name': 'Daniel Smith',
     'department': 'Accounting',
     'birthday': 'May'},
]

with open('employees.csv', 'w') as table:
    headers = ['Name', 'Department', 'Birthday month']
    writer = csv.writer(table)  # объект, который записывает в таблицу
    writer.writerow(headers)  # записываю заголовки как первую строчку в таблицу

"""
Информация в CSV-таблицы записывается построчно. 
Чтобы добавить новую строку в таблицу, нужно: 
1. сформировать список значений 
2. Обратиться к writer'у и вызвать функцию writerow,
которой нужно передать в аргументе список, записываемый как строка 
"""
