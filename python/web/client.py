#!/usr/bin/env python3
# debug_entry = ../index.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print(s.recv(1024))
s.close()

print('--------------------------->')
