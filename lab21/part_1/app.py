from api import API
from middleware import Middleware

app = API()


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        req.environ["Surname"] = 'Kopiievyi'

    def process_response(self, req, resp):
        print("Processing response simple", req.url)


class AnotherCustomMiddleware(Middleware):
    def process_request(self, req):
        for key, value in req.environ.items():
            if isinstance(value, str):
                req.environ[key] = value.capitalize()
            else:
                continue
        print("Processing request another", req.url)

    def process_response(self, req, resp):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)
app.add_middleware(AnotherCustomMiddleware)


@app.route("/print_user_info")
def home(request, response):
    remote_address = f'Remote address: {request.environ.get("REMOTE_ADDR", "No remote addres")}'
    surname = f"Surname: {request.environ.get('Surname', 'No surname')}"
    user_agent = f"User Agent: {request.environ.get('HTTP_USER_AGENT', 'No user agent')}"
    the_path = f"Path: {request.environ.get('PATH_INFO', 'No path info')}"
    username = 'USERNAME: BobbyFisher69'

    response.text = f"{username}\b" \
                    f"{remote_address}\b" \
                    f"{surname}\b" \
                    f"{user_agent}\b" \
                    f"{the_path}\b"
