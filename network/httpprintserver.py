
# coding:utf-8

import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
#from SimpleHTTPServer import SimpleHTTPRequestHandler


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            self.send_response(200)
            self.end_headers()
            request_sz = int(self.headers["Content-length"])
            content = self.rfile.read(request_sz)
            print content
        except Exception as e:
            print str(e)

server = BaseHTTPServer.HTTPServer(('', 9999), HttpHandler)

server.serve_forever()