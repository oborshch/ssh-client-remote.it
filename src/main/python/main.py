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


now = datetime.datetime.now()
global date_log
date_log = str(now.strftime("%d-%m-%Y %H:%M:%S"))


''' authentication '''

def authentication():

    def validateLogin(username, password, webtoken):
        global data
        webtokensrv = str(webtoken.get())
        data = json.loads(urlopen('https://coderlog.top/cdlsrv/srv.php?token='+webtokensrv).read().decode("utf-8"))
        get_token(username.get(), password.get())
        tkWindow.destroy()
    tkWindow = Tk()  
    tkWindow.geometry('300x110')  
    tkWindow.title('CDLSRV | Login remote.it account')

    usernameLabel = Label(tkWindow, text="Username").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username, width=30).grid(row=0, column=1)
    

    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*', width=30).grid(row=1, column=1)  
    


    webtokenLabel = Label(tkWindow,text="Web token").grid(row=2, column=0)  
    webtoken = StringVar()
    webtokenEntry = Entry(tkWindow, textvariable=webtoken, width=30).grid(row=2, column=1) 


    ''' Keep track of the checkbox and save your login data '''
    save_data = BooleanVar()
    check = Checkbutton(tkWindow, text='Remember me', variable=save_data).grid(row=3, column=0)  

    def on_change(*args):
        save = {'login': str(username.get()), 'password': str(password.get()), 'token': str(webtoken.get())}
        with open('user_data.json', 'w') as f:
            f.write(json.dumps(save))

    save_data.trace('w', on_change)

    if (path.exists("user_data.json")):
        with open('user_data.json') as f:
            file_content = f.read()
            user_data = json.loads(file_content)
        username.set(user_data['login'])
        password.set(user_data['password'])
        webtoken.set(user_data['token'])

    validateLogin = partial(validateLogin, username, password, webtoken)
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
    
    tkWindow.mainloop()


''' Logging '''

def logger():
    logging.basicConfig(
        format='|%(levelname)s|%(name)s|%(process)d:%(processName)s| %(lineno)d:%(funcName)s:%(filename)s %(message)s|%(pathname)s|',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(data['log_dir']+"/"+data['log_file'], 'a', 'utf-8'),
            logging.StreamHandler()
        ])
    return logging
 

''' Get token '''

def get_token(username, password):
    logger().info(" | "+date_log+" | Get token | Username: "+os.getlogin())

    headers = {
        "developerkey": data['developerkey']
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
        "developerkey": data['developerkey'],
        "token": token
    }
    body = {
        "deviceaddress": data['deviceaddress'],
        "wait": data['wait'],
        "hostip":data['hostip']
    }

    response = requests.post(data['url'], data=json.dumps(body), headers=headers)
    response_body = response.json()

    server = response_body['connection']['proxyserver']
    port = response_body['connection']['proxyport']
    
    logger().info(" | "+date_log+" | Connect to server: "+server+":"+port+" | Username: "+os.getlogin())
    os.system('wt ssh '+data['username']+'@'+ server + ' -p'+port)



authentication()
logger().info(" | "+date_log+" | Start CDLSRV Client | Username: "+os.getlogin())
connect()