import json


with open('number.json') as json_file:
    content = json.load(json_file)  # чтение с преобразованием в список
    print(content[2])
    print(type(content))


