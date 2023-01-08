from part_1.middleware import Middleware


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
