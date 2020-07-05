#! /usr/bin/python3
# Уроки для этого.
# https://www.youtube.com/watch?v=45OYwgmWqmc&feature=emb_logo

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response
import time
import datetime
import requests

'''Мессенджер на flask + request + PyQT5'''

app = Flask(__name__)
app.secret_key = 'some_secret'

# Массив наших сообщений, со временем будем работать как с типом float от 1970 как основания Unix
messages = [
    # {
    #     "username": "johny",
    #     "text": "Hello World !",
    #     "time": time.time()
    # }
]

# Глоб Словарь всех пользователей
users = {
    # username:password
    'jack': 'blak',
    'mary': '123'
}



@app.route('/')
def page_index():
    return 'Hello World!'





@app.route("/history")
def history():
    """
    Возвращает историю всех сообщений чата.
    request: ?after=float(время параметром get в формате float)
    response: {
        "messages": [
            {"username":"str", "text":"str", "time":float}
            ....
        ]
    }
    """
    after = float(request.args['after'])
    filter_messages = []

    for message in messages:
        if message['time'] > after:
            filter_messages.append(message)

    return {'messages': filter_messages}





@app.route("/send", methods=['POST'])
def send_message():
    '''Получаем json из тела запроса, в json должны быть след данные.
    На основе имени и пароля аутентифицируем пользователя.
    request: {"username":str, "password":str "text":"str"}
    response: {"ok":true}
    '''
    data = request.json # JSON -> dict

    username = data['username']
    password = data['password']
    text = data['text']

    # Авторизация пользователя
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    # Добавим новое сообщение в наш глобальный список сообщений
    messages.append({'username': username, 'text': text, 'time': time.time()})
    print('========')
    print(messages)
    print('=======')
    return {'ok': True}






@app.route('/status')
def page_status():
    '''Тестовый метод'''
    response = make_response(
        {
            "status":"OK",
            "None was set here, now here = ":None,
            'time':time.ctime(),
            'datetime':datetime.datetime.now(),
            'users': len(users),
            'messages': len(messages),
        },
        200
    )
    return response



# Запуск всего приложения, в случае если приложение запущено как основное, а не как модуль
if __name__ == "__main__":
    app.run(debug=True, port=5000)





'''
Для работы с Descktop используем модуль PQ и его дизайнер QT Disigner 

Таким способом можно добавить заголовки к обьекту ответа
response.headers['Sergio'] = 'Popckov'

Таким образом можно поменять статус ответа
response.status_code = 401
'''