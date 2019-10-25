#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import os
from urllib.parse import urlparse

__version__ = "0.1"

class HereProxyHandler(http.server.BaseHTTPRequestHandler):

    server_version = "HereProxyHandler/" + __version__

    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()
        self.directory = directory
        super().__init__(*args, **kwargs)

    def do_GET(self):
        __import__('pdb').set_trace()
        filepath = self.translate_path(self.path)
        # TODO Here
        pass

    def do_HEAD(self):
        pass

    def translate_path(self, path=""):
        # http://localhost:3000/path/to/file
        # =>
        # pwd/path/to/file
        filepath = self.directory + path
        return filepath

def run_server(handler_class=HereProxyHandler):
    httpd = http.server.HTTPServer(("", 3000), handler_class)
    httpd.serve_forever()

def main():
    run_server()

if __name__ == '__main__':
    main()
