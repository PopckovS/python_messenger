#! /usr/bin/python3

#
import PyQt5

# Импортируем микро-сервис flask
from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response

# Импортируем модуль для работы со временем
import time
import datetime

# Импортируем модуль c протоколом http
import requests

# Импортирую Модуль для работы с Базами Данных SQLAlchemy
import sqlalchemy

"""
Мессенджер на flask + request + PyQT5

Установка SQLalchemy
    pip3 install sqlalchemy
    
Уроки для этого : 
    https://www.youtube.com/watch?v=45OYwgmWqmc&feature=emb_logo

обновление pip3 может понадобится для установки свежих модулей на Python.
    sudo -H pip3 install --upgrade pip

Дизайнер PyQt5 поставляется вместе с набором инструментов, установим их:
    sudo apt-get install python3-pyqt5
    sudo apt-get install qttools5-dev-tools

После создания нужного desktop приложения:
    сохранений для послед использования как messenger.ui представляет из себя файл с мета разметкой xml. 
    для преобразования xml файла в Python код импортируем и используем модуль "import PyQt5" 
    Используем команду:
        pyuic5 messenger.ui -o main_window.py
    Чтобы преобразовать xml в python код класс, и функции для работы как с Python кодом.
    
Далее добавим в код след, и это запустит приложение в работу.

    class Ui_MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
    
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()    
    
    
"""





app = Flask(__name__)
app.secret_key = 'some_secret'

# Массив наших сообщений, со временем будем работать как с типом float от 1970 как основания Unix
# TODO если в массиве нету сообщений вабще, то сервер упадет с ошибкой
messages = [
    {
        "name": "johny",
        "text": "Hello World !",
        "time": time.time()
    }
]

# Глоб Словарь всех пользователей
users = {
    # username:password
    'sergio': '123',
    'jojo': '123'
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

    # ==========================
    return {'messages': messages}
    # ==========================

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
    # data = request.json # JSON -> dict

    name = request.json['name']
    password = request.json['password']
    text = request.json['text']

    for token in [name, password, text]:
        if not isinstance(token, str) or not token or len(token) > 1024:
            abort(400)

    # Авторизация пользователя
    if name in users:
        # Если пароль неверен то кидаем ошибку авторизации
        if users[name] != password:
            abort(401)
    else:
        # Создание нового пользователя
        users[name] = password

    # Добавим новое сообщение в наш глобальный список сообщений
    messages.append({'name': name, 'text': text, 'time': time.time()})
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




def filter_dicts(elements, key, min_value):
    new_elements = []

    for element in elements:
        if element[key] > min_value:
            new_elements.append(element)
    return new_elements



@app.route('/messages')
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        abort(400)
    filtered_messages = filter_dicts(messages, key='time', min_value=after)
    return {'messages': filtered_messages}


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