
from logging import root
import requests
import json
import tkinter as tk
from tkinter import *

def mainscreen():
    global root
    global en
    global en2
    global tx
    root = Tk()
    root.geometry("575x375")
    Label(root,text="Ведіть ID користувача").pack()
    en =  Entry(root,)
    en.pack()
    Label(root,text="Ведіть сумму поповнення").pack()
    en2 =  Entry(root)
    en2.pack()
    Label(root,text="Результат операції").pack()
    tx =  Label(root,width="17",height="7")
    tx.pack()
    Button(root,text="Поповнити",command=deepscreen).pack()

def deepscreen():
    global root1
    global json
    global res
    global setbalance
    global id
    global bal
    id = en.get()
    bal = en2.get()
    res = StringVar
    root1 = Toplevel(root)
    setbalance = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(id, bal)
    res = requests.get(setbalance)
    url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(id)

    res = requests.get(url)
    json = res.json()
    for y in json:
        id = y["id"]
        name = y["name"]
        surname = y["surname"]
        email = y["email"]
        school_group = y["school_group"]
        status = y["status"]
        balance = y["balance"]

        if y["id"] is None:
            tx.config(text="Такого ID ну існує")
        else:
            tx.config(text="ID: {}\nName: {}\nSurname: {}\nEmail: {}\nGroup: {}\nStatus: {}\nBalance: {}".format(id, name, surname, email, school_group, status, balance))


mainscreen()
root.mainloop()