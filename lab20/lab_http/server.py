import cgi
from http.server import HTTPServer, SimpleHTTPRequestHandler
import contextlib

from pyowm import OWM

hostName = "localhost"
serverPort = 8800


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'client_form_to_send.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    @staticmethod
    def get_weather(city_name: bytes) -> dict:
        owm = OWM('0ec57f389f38e848202eafdc9373c18e')  # You MUST provide a valid API key
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(f'{city_name}')
        return observation.weather

    def do_POST(self):  # sourcery skip: last-if-guard
        if self.path == '/weather':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            if ctype == 'multipart/form-data':
                try:
                    fields = cgi.parse_multipart(self.rfile, pdict)

                    file_to_open = open('client_form_to_receive.html').read()
                    self.send_response(200)
                    city_name = fields.get('city_name')[0]

                    weather_cast = self.get_weather(city_name=city_name)
                    status = weather_cast.__dict__.get('status')
                    detailed_status = weather_cast.__dict__.get('detailed_status')
                    wind = weather_cast.__dict__.get('wnd')
                    humidity = weather_cast.__dict__.get('humidity')
                    pressure = weather_cast.__dict__.get('pressure')
                    temperature = weather_cast.temperature('celsius')

                    file_to_open = file_to_open.format(status=status, detailed_status=detailed_status,
                                                       wind=wind, humidity=humidity, pressure=pressure,
                                                       temperature=temperature,**fields)

                except Exception as e:
                    file_to_open = "File Not Found"
                    print(e)
                    self.send_response(404)

                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    with contextlib.suppress(KeyboardInterrupt):
        webServer.serve_forever()

    webServer.server_close()
    print("Server stopped.")
