from api import API
from part_1.custom_middlewares.simple import SimpleCustomMiddleware, AnotherCustomMiddleware

# gunicorn -b 127.0.0.1:8181 app:app
app = API()


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
