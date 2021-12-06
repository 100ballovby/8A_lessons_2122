import requests
import json

url = 'https://api.github.com/'  # сохраняю ссылку для подключения
response = requests.get(url)  # подключаюсь к серверу по ссылке url
print(response)  # узнаю статус подключения

json_response = response.json()  # превращаю ответ сервера в JSON файл
for key, value in json_response.items():  # перебираю весь ответ сервера
    print(f'Название: "{key}", ссылка: "{value}"')  # вывожу полученный ответ


