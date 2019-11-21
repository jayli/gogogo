#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
from urllib.parse import urlparse

class LocalFileHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        uri = urlparse(self.path)
        print(uri)
        self.wfile.write(b"hello world")

def main():
    Port = 3000
    try:
        server = http.server.HTTPServer(("", Port), http.server.SimpleHTTPRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

if __name__ == '__main__':
    main()
