#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
from http import HTTPStatus
import os
import json
import pprint as pp
import re
import time
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
        filepath = self.translate_path()
        dirname = os.path.dirname(filepath)
        basename = os.path.basename(filepath)
        if trim(basename) == "":
            # TODO dir access
            dir_list = os.scandir(dirname)
            print_dir_list(dir_list)
            date_time = str(time.time())
            body = ("Date time: " + date_time).encode("utf-8")
            length = str(len(body))
            __import__('pdb').set_trace()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-Length", length)
            self.end_headers()
            self.wfile.write(body)
            pass

        if trim(basename) != "":
            pass

        # TODO Here
        pass

    def do_HEAD(self):
        pass

    def translate_path(self):
        # http://localhost:3000/path/to/file
        # =>
        # pwd/path/to/file
        filepath = self.directory + self.path
        return filepath

def print_dir_list(it):
    print('---')
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    return None

def trim(msg=""):
    return re.sub(r'(^\s+|\s+$)',"", msg)

def run_server(handler_class=HereProxyHandler):
    httpd = http.server.HTTPServer(("", 3000), handler_class)
    httpd.serve_forever()

def log(msg):
    print(msg)

def main():
    run_server()

if __name__ == '__main__':
    main()
