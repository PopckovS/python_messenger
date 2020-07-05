#! /usr/bin/python3
import requests
from pprint import pprint

response = requests.get('http://localhost:5000/status')
print('========== http://localhost:5000/status Вывод статуса ===========')
pprint(response.json())



response = requests.get('http://localhost:5000/history')
print('========= http://localhost:5000/history Вывод Истории ============')
pprint(response.json())



response = requests.post(
    'http://localhost:5000/send',
    json={"username": "Sergio", "text": "Hello"}
)
print('=========http://localhost:5000/send Делаем post запрос и получаем ответ ============')
pprint(response.json())




response = requests.get('http://localhost:5000/history')
print('========= http://localhost:5000/history Вывод Истории ============')
pprint(response.json())
















'''
Пример отправки Request запроса к серверу методом GET на localhost:5000 
получение и вывод результата при помощи модуля requests

response = requests.get('http://localhost:5000/status')

print('*====== Начало ответ ======*')
print('Ответ: {response}'.format(response=response))
print('----------------')
print('Статус код: {status_code}'.format(status_code=response.status_code))
print('----------------')
print('Заголовки ответа:')
for head in response.headers:
    print(head + ' = ' + response.headers[head])
print('----------------')
print('Тело ответа: {body}'.format(body=response.text))
print('*====== Конец ответ ======*')

'''

