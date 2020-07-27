#! /usr/bin/python3

import os
import time
from time import sleep
from subprocess import *

class Install():
    """Класс для начальной настройки приложения
    Клонирование проекта из репозитория github
    Установка начальных модулей для работы приложения
    """

    def __init__(self, repo):
        """Начальная инициализация проекта, установка приложения и вход в рабочую директорию"""
        self.repo = repo
        self.direction = self.cut_str(repo)


        # Вызываем методы для установки всех зависимостей
        self.composer_install()

        # Установка репозитория из gitHub
        self.clone_github_repo()


        # call(["cd", "python_messenger"])
        # os.system("cd python_messenger")

        # self.shell_execute('cd python_messenger')
        # python_messenger
        

    def composer_install(self):
        """Шутка для php-шников, но давыполняет туже функцию устанавливает все зависимости проекта"""
        self.pip_upgrae()
        self.pip_sqlalchemy()
        self.pip_flask()
        self.pip_pq5()
        self.pip_dev_tools()

    def clone_github_repo(self):
        """Клонирование и установка проекта из репозитория на github"""
        self.shell_execute(f"git clone {self.repo}")


    def shell_execute(self, command, stop=0):
        """Исполнение указанной команды в shell оболочке
        или выкинуть исключение с указанием команды в которой возникла ошибка
        """
        try:
            os.system(command)
        except:
            os.system('Error in {error}'.format(error=command))

        # приостановка выполнения скрипта
        if isinstance(stop, int) and stop > 0:
            sleep(stop)



    def pip_upgrae(self):
        """Обновление pip утилиты Python """
        self.shell_execute("sudo -H pip3 install --upgrade pip")

    def pip_sqlalchemy(self):
        """Установка SQLAlchemy это ORM для работы с БД"""
        self.shell_execute("pip3 install sqlalchemy")

    def pip_flask(self):
        """Установка Микро сервиса Flask"""
        self.shell_execute("pip3 install Flask")

    def pip_pq5(self):
        """Установка PQ5 для работы десктопного приложения программы"""
        self.shell_execute("sudo apt-get install python3-pyqt5 -y")

    def pip_dev_tools(self):
        """Установка PQ5 Desiner я возможности редактирования десктопной программы"""
        self.shell_execute("sudo apt-get install qttools5-dev-tools -y")


    def cut_str(self, repository):
        """Обрезает принятый URL репозитория с github и получаеет название проекта/рабочей директории"""
        result = repository.rsplit('.', 2)
        result = result[1].rsplit('/', 1)
        print(result[1])
        return result[1]

# ./desktop_start.py


application = Install("https://github.com/PopckovS/python_messenger.git")

