from api import API
from middleware import Middleware

app = API()


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        print('Processing request', req.url)

    def process_response(self, req, resp):
        print("Processing response", req.url)


app.add_middleware(SimpleCustomMiddleware)


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"


@app.route("/sum/{num_1}/{num_2}")
def sum_all(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"


@app.route("/type/{word_1}/{word_2}")
def sum_all(request, response, word_1, word_2):
    response.text = f"{word_1} {word_2}" * 100
