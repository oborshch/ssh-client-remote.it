from fbs_runtime.application_context.PyQt5 import ApplicationContext
import requests
import json
import os
import subprocess
import ctypes
import logging
import datetime
import stun
from urllib.request import urlopen
from tkinter import *
from functools import partial
from os import path
import webbrowser


now = datetime.datetime.now()
global date_log
date_log = str(now.strftime("%d-%m-%Y %H:%M:%S"))


''' authentication '''

def authentication():

    def validateLogin(username, password, deviceaddress, developerkey, sshusername):
        global data
        global key
        global service
        global login
        
        key = developerkey.get()
        service = deviceaddress.get()
        login = sshusername.get()
        with open('user_data.json') as f:
            file_content = f.read()
            data = json.loads(file_content)
        get_token(username.get(), password.get(), developerkey.get())
        tkWindow.destroy()
    def faq():
        return webbrowser.open('https://github.com/alexborsch/ssh-client-remote.it')

    tkWindow = Tk()  
    tkWindow.geometry('330x180+300+300')
    tkWindow.resizable(width=False, height=False)
    tkWindow.iconbitmap('Icon.ico')  
    tkWindow.title('CDLSRV | Login remote.it account')

    ''' remote.it login '''
    usernameLabel = Label(tkWindow, text="Username").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username, width=30).grid(row=0, column=1)
    
    ''' remote.it password '''
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*', width=30).grid(row=1, column=1)  
    
    ''' remote.it device address '''
    deviceaddressLabel = Label(tkWindow,text="Device address").grid(row=2, column=0)  
    deviceaddress = StringVar()
    deviceaddressEntry = Entry(tkWindow, textvariable=deviceaddress, width=30).grid(row=2, column=1) 
    
    ''' Developer key '''
    developerkeyLabel = Label(tkWindow,text="Developer key").grid(row=3, column=0)  
    developerkey = StringVar()
    developerkeyEntry = Entry(tkWindow, textvariable=developerkey, width=30).grid(row=3, column=1)

    ''' SSH username '''
    sshusernameLabel = Label(tkWindow,text="SSH username").grid(row=4, column=0)  
    sshusername = StringVar()
    sshusernameEntry = Entry(tkWindow, textvariable=sshusername, width=30).grid(row=4, column=1)

    ''' Keep track of the checkbox and save your login data '''
    save_data = BooleanVar()
    check = Checkbutton(tkWindow, text='Remember me', variable=save_data).grid(row=5, column=0)  

    def on_change(*args):
        save = {'login': str(username.get()), 'password': str(password.get()), 'deviceaddress': str(deviceaddress.get()), 'developerkey': str(developerkey.get()), 'sshusername': str(sshusername.get())}
        with open('user_data.json', 'w') as f:
            f.write(json.dumps(save))

    save_data.trace('w', on_change)

    if (path.exists("user_data.json")):
        with open('user_data.json') as f:
            file_content = f.read()
            user_data = json.loads(file_content)
        username.set(user_data['login'])
        password.set(user_data['password'])
        deviceaddress.set(user_data['deviceaddress'])
        developerkey.set(user_data['developerkey'])
        sshusername.set(user_data['sshusername'])

    validateLogin = partial(validateLogin, username, password, deviceaddress, developerkey, sshusername)
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=6, column=0)  
    infoButton = Button(tkWindow, text="FAQ", command=faq).grid(row=6, column=1)
    tkWindow.mainloop()


''' Logging '''

def logger():
    logging.basicConfig(
        format='|%(levelname)s|%(name)s|%(process)d:%(processName)s| %(lineno)d:%(funcName)s:%(filename)s %(message)s|%(pathname)s|',
        level=logging.INFO,
        handlers=[
            logging.FileHandler('logs/cdl.log', 'a', 'utf-8'),
            logging.StreamHandler()
        ])
    return logging
 

''' Get token '''

def get_token(username, password, developerkey):
    logger().info(" | "+date_log+" | Get token | Username: "+os.getlogin())

    headers = {
        "developerkey": developerkey
    }
    body = {
        "password": password,
        "username": username
        
    }

    url = "https://api.remot3.it/apv/v27/user/login"

    response = requests.post(url, data=json.dumps(body), headers=headers)
    response_body = response.json()
    statuscode = str(response.status_code)
    if (statuscode == '200'):
        global token
        token = response_body['token']
        logger().info(" | "+date_log+" | Get token:  OK| Username: "+os.getlogin())
    else:
        
        logger().error(" | "+date_log+" | Token error! Status Code: "+statuscode+"| Username: "+os.getlogin())
        ctypes.windll.user32.MessageBoxW(0, "Token error! Status Code: "+statuscode, 1)


''' Connect to server '''

def connect():
    headers = {
        "developerkey": key,
        "token": token
    }
    body = {
        "deviceaddress": service,
        "wait": 'true',
        "hostip": '0.0.0.0'
    }

    response = requests.post('https://api.remot3.it/apv/v27/device/connect', data=json.dumps(body), headers=headers)
    response_body = response.json()

    server = response_body['connection']['proxyserver']
    port = response_body['connection']['proxyport']
    
    logger().info(" | "+date_log+" | Connect to server: "+server+":"+port+" | Username: "+os.getlogin())
    os.system('wt ssh '+login+'@'+ server + ' -p'+port)
    


''' App status and info '''

def work():
    tkWindow = Tk()  
    tkWindow.geometry("420x362+300+300")
    tkWindow.resizable(width=False, height=False)
    tkWindow.iconbitmap('Icon.ico')  
    tkWindow.title('CDLSRV | Connection status')

    ''' remote.it login '''
    statusLabel = Label(tkWindow, text="Connection status").grid(row=0, column=0)
    calculated_text = Text(tkWindow, height=14, width=50)
    calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)

    scrollb = Scrollbar(tkWindow, command=calculated_text.yview)
    scrollb.grid(row=4, column=4, sticky='nsew')
    calculated_text.configure(yscrollcommand=scrollb.set)
    username = StringVar()
    tkWindow.mainloop()


authentication()
logger().info(" | "+date_log+" | Start CDLSRV Client | Username: "+os.getlogin())
work()
connect()