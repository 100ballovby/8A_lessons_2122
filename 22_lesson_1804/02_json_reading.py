import json


with open('series_SUGAR.json') as file:
    data = json.loads(file.read())
    for price in data['data']['rates']:
        key = data['data']['rates'][price]
        try:
            print(price, key['SUGAR'] * 0.45, 'кг')
        except KeyError:  # если возникает ошибка ключа
            pass
