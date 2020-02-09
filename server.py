
# -*- coding: utf-8 -*-
#test on python 3.4 ,python of lower version  has different module organization.
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import socketserver

PORT = 8080
ADDRESS="0.0.0.0"

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

# Handler = http.server.
Handler = CORSRequestHandler

Handler.extensions_map={
    '.manifest': 'text/cache-manifest',
	'.html': 'text/html',
    '.png': 'image/png',
	'.jpg': 'image/jpg',
	'.svg':	'image/svg+xml',
	'.css':	'text/css',
	'.js':	'application/javascript',
    '.wasm': 'application/wasm',
    '.data': 'application/octet-stream',
	'': 'application/octet-stream', # Default
    }

httpd = socketserver.TCPServer((ADDRESS, PORT), Handler)

print(f"serving at http://{ADDRESS}:{PORT}")
httpd.serve_forever()
