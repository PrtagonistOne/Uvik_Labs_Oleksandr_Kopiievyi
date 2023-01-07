import cgi
from http.server import HTTPServer, SimpleHTTPRequestHandler
import contextlib

hostName = "localhost"
serverPort = 8800


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'client_form_to_send.html'
            self.headers['content-type'] = 'multipart/form-data'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/weather':

            ctype = cgi.parse_header(self.headers.get('content-type'))
            print(ctype)
            html = "<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    with contextlib.suppress(KeyboardInterrupt):
        webServer.serve_forever()

    webServer.server_close()
    print("Server stopped.")
