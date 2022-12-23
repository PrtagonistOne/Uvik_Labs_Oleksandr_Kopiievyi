from http.server import HTTPServer, SimpleHTTPRequestHandler
import contextlib

hostName = "localhost"
serverPort = 8800


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'client_form_to_send.html'
        return SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    with contextlib.suppress(KeyboardInterrupt):
        webServer.serve_forever()
    webServer.server_close()
    print("Server stopped.")
