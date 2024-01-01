from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os
os.system("start http://127.0.0.1:8000/data/setup.html?Token=NoDeta")
print("open 8000 port")
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	def do_HEAD(self):
		self._set_headers()
	def do_GET(self):
		self._set_headers()
		print(self.path)
		#print(parse_qs(self.path[2:]))
		self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
	def do_POST(self):
		self._set_headers()
		form = cgi.FieldStorage(
			fp=self.rfile,
			headers=self.headers,
			environ={'REQUEST_METHOD': 'POST'}
		)
		print(form.getvalue("foo"))
		print(form.getvalue("bin"))
		self.wfile.write("<html><body><h1>POST Request Received!</h1></body></html>")

server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()