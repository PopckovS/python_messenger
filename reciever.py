#! /usr/bin/python3

import requests
import time
from time import sleep
from pprint import pprint
import os
from datetime import datetime

counter_request = 0
last_time_of_message = 0

while True:
    counter_request += 1
    response = requests.get(
        'http://127.0.0.1:5000/history',
        params={'after': last_time_of_message}
    )
    data = response.json()
    # print('/*-------------- Запрос {counter_request} -------------*/'.format(counter_request=counter_request))
    counter_msg = 0
    for message in data['messages']:
        counter_msg += 1
        beauty_time = datetime.fromtimestamp(message['time'])
        # print('---- №{counter_msg} ----'.format(counter_msg=counter_msg))
        print('=========================')
        print('Имя : ' + message['username'])
        print('Сообщение : ' + message['text'])
        print('Время : ' + beauty_time.strftime('%Y:%m:%d %H:%M:%S'))
        last_time_of_message = message['time']

    sleep(1)

