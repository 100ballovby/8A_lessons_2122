import json
import csv


with open('series_SUGAR.json') as file:
    data = json.loads(file.read())
    headers = ['Date', 'In lb', 'In Kg', 'Amount $']
    with open('sugar_price.csv', 'w', encoding='utf8', newline='') as table:
        writer = csv.writer(table)
        writer.writerow(headers)
        for price in data['data']['rates']:
            line = []
            key = data['data']['rates'][price]
            try:
                amount_lb = key['SUGAR']
                amount_kg = amount_lb * 0.45
                line.append(price)
                line.append(amount_lb)
                line.append(amount_kg)
                line.append(1)
                writer.writerow(line)
            except KeyError:  # если возникает ошибка ключа
                pass
