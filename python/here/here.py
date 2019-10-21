#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import http.server
from urllib.parse import urlparse

def runServer(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler):
    server_addr = ("", 3000)
    httpd = server_class(server_addr, handler_class)
    httpd.serve_forever()

def main():
    runServer()

if __name__ == '__main__':
    main()
