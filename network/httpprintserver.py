
# coding:utf-8
import sys

if sys.version_info.major ==2:
    from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
else:
    from http.server import BaseHTTPRequestHandler,HTTPServer

class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            self.send_response(200)
            self.end_headers()
            request_sz = int(self.headers["Content-length"])
            content = self.rfile.read(request_sz)
            print (content)
        except Exception as e:
            print (str(e))

server = HTTPServer(('', 80), HttpHandler)

server.serve_forever()