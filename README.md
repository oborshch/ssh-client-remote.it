# CDLSRV v.0.1.354

## Content

* About the program 
* Installation
* Installation from source code
* First launch
* Logging
* Dependencies
* ToDo


## About the program 

CDLSRV - utility to connect to the home server via SSH using remote.it service

**ATTENTION!** The process of registration and connection to remote.it service will not be described in this one.
documentation. Detailed information can be found at the official [library](https://docs.remote.it/) website . 
remote.it. service. Also on your server should be configured to connect via SSH.
All this is written in remote.it [documentation](https://docs.remote.it/) .

If you already use the remote.it service to connect to your home server then
you know that for each connection you need to log in to your account and generate 
address for connection. This is not always convenient. So I decided to automate this process. 


## Installation

The installation of the program is very simple. [Download](https://github.com/alexborsch/ssh-client-remote.it/releases/tag/0.1.354) the installer, run it and wait for the installation to complete.

## Installation from source code

If you want to be the first to try the new features of the program, you can build it yourself from the source code.

> The Python fbs library is used for development, building exe and other amenities.

Installation:
```
git clone https://github.com/alexborsch/ssh-client-remote.it.git
cd ssh-client-remote.it
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

Launch:
```
fbs run
```

Assembly of an exe/installer:
```
fbs freeze
fbs installer
```

## First run

Authorization window:<br>
![Main Window](https://coderlog.top/github/images/main_window.png)<br>

You will receive the authorization data in your profile at remote.it!<br>
Description of login fields:<br>
**Username** - account login (email)<br>
**Password** - account password<br>
**Device address** - The Service ID of your connection can be found in a pop-up window when you click on the connected device.<br>
![Device address](https://coderlog.top/github/images/service_id.png)<br>
**Developer key** - This is your unique developer API key for using and accessing remote.it API. Do not share it with anyone. You can find it in your account settings:<br>
![Device address](https://coderlog.top/github/images/devkey.png)<br>
**SSH Username** - user login on your server<br>
**Remember me** - checkbox to save all authorization data into configuration file
After filling in all fields, press **Login**.
If all fields are filled in correctly, you will be logged in and the **Windows terminal** window will open asking you to enter a password from your server user account.
The terminal may also ask for permission to trust the server, for which you need to enter **yes**.
After that you will be authorized on your server without using the remote.it web interface:<br>
![Device address](https://coderlog.top/github/images/term.png)<br>

## Logging
The program contains logging in the file /logs/cdllog.log.
It records data on errors, successful start and receipt of a one-time token, address and port to connect to the server. In this file you can learn about errors 
on CDLSRV
**AUTHORIZATION DATA, USER DATA, WORK ON YOUR SERVER, CDLSRV PROGRAM ARE NOT LOGGED IN**.

## Dependencies/ Software used

**Python 3.6.8** [Download](https://www.python.org/downloads/release/python-368/)<br>
**NSIS 3.06.1** [Download](https://sourceforge.net/projects/nsis/files/NSIS%203/3.06.1/)<br>
**Windows Terminal 1.2.2381.0** [Windows store](https://www.microsoft.com/uk-ua/p/windows-terminal/9n0dx20hk701) | [GitHub](https://github.com/microsoft/terminal)<br>

## ToDo
* Encryption of user data entered during authorization
* Linux, macOS support
* Support for Samba server
* WEB Server Apache/Nginx support


-----

## Содержание

* О программе 
* Установка
* Установка из исходного кода
* Первый запуск
* Логирование
* Зависимости
* ToDo


## О программе 

CDLSRV - утилита для подключения к домашнему серверу по SSH используя сервис remote.it

**ВНИМАНИЕ!** Процесс регистрации и подключения к сервису remote.it не будет описан в этой
документации. Подробную информацию вы можете узнать на сайте официальной [библиотеке](https://docs.remote.it/) 
сервиса remote.it. Так же на вашем сервере должно быть настроенно подключение по SSH.
Обо всем этом написанно в документации [remote.it](https://docs.remote.it/)

Если вы уже используете сервис remote.it для подключения к своему домашнему серверу то
вы знаете что для каждого подключения вам нужно заходить в свой аккаунт и генерировать 
адресс для подключения. Это не всегда удобно. По этому я решил автоматизировать этот процесс. 


## Установка

Установка программы очень простая. Скачиваете [инстралятор](https://github.com/alexborsch/ssh-client-remote.it/releases/tag/0.1.354) , запускаете и дожидаетесь окончания установки

## Установка из исходного кода

Если вы хотите первыми испробовать новые возможности программы, то можете сами собрать её из исходного кода.

> Для разработки, сборки exe и прочего удобства используется Python библиотека fbs

Установка:
```
git clone https://github.com/alexborsch/ssh-client-remote.it.git
cd ssh-client-remote.it
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

Запуск:
```
fbs run
```

Сборка exe/инсталятора:
```
fbs freeze
fbs installer
```

## Первый запуск

Окно авторизации:<br>
![Main Window](https://coderlog.top/github/images/main_window.png)<br>

Данные для авторизации вы получите в своём профиле на remote.it!<br>
Описание полей авторизации:<br>
**Username** - логин учетной записи (email)<br>
**Password** - пароль учётной записи<br>
**Device address** - Service ID вашего подключения можно найти в сплывающем окне при нажатии на подключённое устройство.<br>
![Device address](https://coderlog.top/github/images/service_id.png)<br>
**Developer key** - Это ваш уникальный ключ API разработчика для использования и доступа к remote.it API. Не делитесь им ни с кем. Найти его можете в настройках аккаунта:<br>
![Device address](https://coderlog.top/github/images/devkey.png)<br>
**SSH Username** - логин пользователя на вашем сервере<br>
**Remember me** - чекбокс для сохранения всех данных авторизации в конфигурационный файл
После заполнения всех полей нажимаем **Login**
Если все поля заполненны правильно, произойдёт авторизация и откроется окно **Windows terminal** с предложением ввести пароль от учетной записи пользователя вашего сервера.
Также терминал может запросить разрешение доверия серверу, на что нужно ввести **yes**
После чего вы будете авторизированы на вашем сервере без использования веб интерфейса remote.it:<br>
![Device address](https://coderlog.top/github/images/term.png)<br>

## Логирование
В программе присутствует логирование в файл /logs/cdllog.log
В него записываются данные об ошибках, успешном запуске и получению одноразового токена, адресс и порт для подключения к серверу. В этом файле можно узнать об ошибках 
в работе CDLSRV
**ДАННЫЕ АВТОРИЗАЦИИ, ПОЛЬЗОВАТЕЛЬСКИЕ ДАННЫЕ, РАБОТА НА ВАШЕМ СЕРВЕРЕ, ПРОГРАММОЙ CDLSRV НЕ ЗАПИСЫВАЮТСЯ В ЛОГ ФАЙЛЫ**

## Зависимости/Используемое ПО

**Python 3.6.8** [Скачать](https://www.python.org/downloads/release/python-368/)<br>
**NSIS 3.06.1** [Скачать](https://sourceforge.net/projects/nsis/files/NSIS%203/3.06.1/)<br>
**Windows Terminal 1.2.2381.0** [Windows store](https://www.microsoft.com/uk-ua/p/windows-terminal/9n0dx20hk701) | [GitHub](https://github.com/microsoft/terminal)<br>

## ToDo
* Шифрование пользовательских данных вводимых при авторизации
* Поддержка Linux, macOS
* Поддержка Samba server
* Поддержка WEB Server Apache/Nginx