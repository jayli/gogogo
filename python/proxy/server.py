#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import http.server
import socketserver

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        __import__('pdb').set_trace()
        uri = urlparse(self.path)
        print(uri)
        self.wfile.write("123")

def main():
    """docstring for main"""
    Port = 3000

    # Handler = http.server.SimpleHTTPRequestHandler

    try:
        server = http.server.HTTPServer(("", Port), Handler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == '__main__':
    main()
