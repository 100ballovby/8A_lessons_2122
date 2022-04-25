import json


def read_json(file, key):
    """
    Читает json файл series и превращает его
    в два списка - даты и стоимость
    :param file: имя файла для открытия
    :param key: ключ, который нужно искать в файле
    :return: списки с данными
    """
    dates = []
    prices = []
    with open(file) as jf:
        data = json.loads(jf.read())
        data = data['data']['rates']  # очищаю словарь от ненужных ключей
        for day in data:
            try:
                prices.append(data[day][key])  # достаю стоимость из словаря и добавляю ее в список
                dates.append(day)  # достаю дату из словаря и добавляю ее в список
            except:
                pass
        return dates, prices


d, p = read_json('series_COTTON.json', 'COTTON')
print(d)
print(p)
