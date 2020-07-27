#! /usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
import main_window
import requests
import time
from datetime import datetime

"""
После генерации класс для десктопного приложения, тут мы его наследуем и в нем определяем
функции по работе с сервером. 
"""

class MessengerWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    """
        Унаследовались от класса сгенерированного на основе main_window.py и запускаем от сюда окно приложения.

        pyuic5 messenger.ui -o main_window.py
    """

    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        # Делаем URL общедоступным в атрибуте класса
        self.url = url

        # Связка кнопки зарегестрированной как pushButton
        # с методом sendMessage который определим в этом классе.
        self.pushButton.pressed.connect(self.sendMessage)

        self.after = time.time() - 24 * 60 * 60

        # Таймер для запуска метода который будет запускаться через некотрый
        # промежуток времени, постоянно опрашивая нашу функцию update_messages
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)




    def add_text(self, text):
        """Метод добавляет сообщения в общий чат"""
        self.textBrowser.append(text.format(end='\n'))
        self.textBrowser.repaint()



    def format_message(self, message):
        """Метод форматирует данные в тот вид в котором данные будут отображены в чате"""
        name = message['name']
        text = message['text']

        # Форматирование даты/времени
        dt = datetime.fromtimestamp(message['time'])
        dt_beauty = dt.strftime('%Y:%m:%d %H:%M:%S')

        # Возвращает форматированные данные
        return f'{name} {dt_beauty}\n{text}\n'



    def update_messages(self):
        # Получаем все сообщения с сервера, после определенной даты времени
        try:
            response = requests.get(f'{self.url}messages', params={'after': self.after})
        except:
            return


        messages = response.json()['messages']
        for message in messages:
            # format_message красиво форматирует данные и передает их в
            # метод add_text который добавляет сообщение в общий чат
            self.add_text(self.format_message(message))

            # Очищаем поле ввода сообщений
            self.textMessage.setText('')

            # Обновляем время с полседнего посланного сообщения
            self.after = message['time']





    def sendMessage(self):
        """Метод для обработки кнопки отправки сообщения
        Отправляет введенное сообщение на сервер
        """

        # Получаем текст из поля для логина
        username = self.lineUserName.text()
        if not username:
            self.add_text('Введите логин')
            return

        # Получаем текст из поля для пароля
        password = self.linePassword.text()
        if not password:
            self.add_text('Введите пароль доступа')
            return

        # Получаем текст из поля для сообщения
        text = self.textMessage.toPlainText()
        if not text:
            self.textBrowser.repaint()
            return

        # Формируем сообщение в словарь,оторый потом станет json телом сообщения
        message = {"name": username, "password": password, "text": text}

        # Проверка на отправку сообщения на сервер
        try:
            response = requests.post(f'{self.url}send', json=message)
        except:
            self.add_text('Сервер не доступен')
            return

        if response.status_code == 200:
            self.add_text('')
        elif response.status_code == 401:
            self.add_text('Не правильный логин/пароль')
        else:
            self.add_text('Ошибка')




# Заппускаем работу всего приложения
app = QtWidgets.QApplication([])
window = MessengerWindow('http://127.0.0.1:5000/')
window.show()
app.exec_()












