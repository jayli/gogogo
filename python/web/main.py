#!/usr/bin/env python3
# debugger_entry = ./main.py
# debugger_entry = ../index.py

from urllib import request
import socket

def init():
    print("---------------->>")
    print("ok")

    resu = request.urlopen("http://www.baidu.com", data=None, timeout=10)
    data = resu.read().decode()

    print(data)

    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print("连接地址:" + str(addr))
        c.send('hello'.encode('utf-8'))
        c.close()

init()
print("---------------DebugEnd---------------->>")
