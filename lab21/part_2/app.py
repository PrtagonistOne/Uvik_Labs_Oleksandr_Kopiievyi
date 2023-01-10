from webob import Response, Request

from api import API, convertable_to_int
from middleware.middleware import Middleware
from db.read import get_all_post_data, get_post_by_id, get_post_by_data
from db.delete import delete_record_by_id
from db.write import create_record, dynamic_update

app = API()
# gunicorn -b 127.0.0.1:8787 app:app


class SimpleCustomMiddleware(Middleware):
    def process_request(self, req):
        req_log_info = f"Processing request - {req.url}"
        print(req_log_info)
        make_logs(request=req, response=Response(), log_info=req_log_info)

    def process_response(self, req, resp):
        resp_log_info = f"Processing response - {req.url}"
        print(resp_log_info)
        make_logs(request=req, response=Response(), log_info=resp_log_info)


app.add_middleware(SimpleCustomMiddleware)


@app.route("/secured")
def make_logs(request: Request, response: Response, log_info: str):
    with open("logs.txt", "a+") as logs_file:
        logs_file.write(log_info + '\n')

    with open('logs.txt', 'r') as log_value:
        response.text = log_value.read()


@app.route("/api/")
def home(request: Request, response: Response):
    if request.headers.environ.get('REQUEST_METHOD') == "GET":
        response.text = "Hello from the api page"


@app.route("/api/posts/")
def get_all_posts(request: Request, response: Response):
    if request.headers.environ.get('REQUEST_METHOD') == "GET" and not request.GET:
        response.json = get_all_post_data()
    elif request.headers.environ.get('REQUEST_METHOD') == "GET" and request.GET:
        post_data = dict(request.GET.items())
        response.json = get_post_by_data(post_data=post_data)
    elif request.headers.environ.get('REQUEST_METHOD') == "POST":
        body_json = convertable_to_int(request)
        created_post_data = create_record(post_data=body_json)

        response.status_code = 201
        response.json = created_post_data


@app.route("/api/posts/{id:d}/")
def get_one_post(request: Request, response: Response, id: int):
    if request.headers.environ.get('REQUEST_METHOD') == "GET":
        response.json = get_post_by_id(_id=id)
    if request.headers.environ.get('REQUEST_METHOD') == "PUT":
        body_json = convertable_to_int(request)
        updated_post_data = dynamic_update(body_json, _id=id)

        response.status_code = 200
        response.json = updated_post_data
    if request.headers.environ.get('REQUEST_METHOD') == "PATCH":
        body_json = convertable_to_int(request)
        updated_post_data = dynamic_update(post_data=body_json, _id=id)

        response.status_code = 200
        response.json = updated_post_data
    if request.headers.environ.get('REQUEST_METHOD') == "DELETE":
        delete_record_by_id(_id=id)
        response.status_code = 204

