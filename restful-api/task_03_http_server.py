#!/usr/bin/python3
"""Simple HTTP Server to handle GET requests"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Simple HTTP Server to handle GET requests"""
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John',
                'age': '30',
                'city': 'New York'
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Ok")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server module"
            }
            self.wfile.write(json.dumps(info).encode())
        else:
            self.send_error(404, 'Endpoint Not Found')


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
