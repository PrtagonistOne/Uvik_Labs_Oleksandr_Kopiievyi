from webob import Response, Request

from api import API, convertable_to_int
from middleware.middleware import Middleware
from db.read import get_all_post_data, get_one_post_datum, get_post_data_by_likes
from db.write import save_to_db, update_record, partial_update
from db.delete import delete_record_by_id

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
    if request.headers.environ.get('REQUEST_METHOD') == "GET":
        response.json = get_all_post_data()
    elif request.headers.environ.get('REQUEST_METHOD') == "POST":
        body_json = convertable_to_int(request)
        save_to_db(body_json)

        response.status_code = 201
        response.json = body_json


@app.route("/api/posts/{id:d}/")
def get_one_post(request: Request, response: Response, id: int):
    if request.headers.environ.get('REQUEST_METHOD') == "GET":
        response.json = get_one_post_datum(id=id)
    if request.headers.environ.get('REQUEST_METHOD') == "PUT":
        body_json = convertable_to_int(request)
        update_record(body_json, id=id)
        response.status_code = 200
        response.json = body_json
    if request.headers.environ.get('REQUEST_METHOD') == "PATCH":
        body_json = convertable_to_int(request)
        partial_update(body_json, id=id)
        response.status_code = 200
        response.json = get_one_post_datum(id=id)
    if request.headers.environ.get('REQUEST_METHOD') == "DELETE":
        delete_record_by_id(id=id)
        response.status_code = 204
        response.text = 'No content'


@app.route("/api/posts")
def get_posts_by_likes(request: Request, response: Response):
    if request.headers.environ.get('REQUEST_METHOD') == "GET":
        likes = dict(request.GET).get('likes')
        response.json = get_post_data_by_likes(likes=int(likes))
