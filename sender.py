#! /usr/bin/python3

import requests
from pprint import pprint

flag = 'N'

# while flag != 'Y':
while True:
    username = input("Введите ваше имя:")
    password = input("Введите ваш пароль доступа:")
    text = input("Введите ваше сообщение:")

    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={"username": username, "password": password, "text": text}
    )
    # print('======== Ответ на наш POST запрос к серверу ========')
    # pprint(response.json())
    if not response.json()['ok']:
        print('Access denied')
        break

    # flag = input('Y/N остановить отправку сообщенйи к серверу ? : ')