#! /usr/bin/python3

import requests
from pprint import pprint

flag = 'N'

username = input("Введите ваше имя:")
password = input("Введите ваш пароль доступа:")

# while flag != 'Y':
while True:

    text = input("Введите ваше сообщение:")

    message = {"username": username,
               "password": password,
               "text": text}
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json=message
    )
    # print('======== Ответ на наш POST запрос к серверу ========')
    # pprint(response.json())
    if not response.json()['ok']:
        print('Access denied')
        break

    # flag = input('Y/N остановить отправку сообщенйи к серверу ? : ')