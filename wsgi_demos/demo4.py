from wsgiref.simple_server import make_server


class Application(object):
    urls = [
        ('/', 'index'),
        ('/hello', 'hello'),
    ]

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        path_info = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']
        for path, name in self.urls:
            if path == path_info:
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func()
        return self.notfound()

    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8')]
        self.start_response(status, response_headers)
        yield b"Welcome!\n"

    def GET_hello(self):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8')]
        self.start_response(status, response_headers)
        yield b"Hello world!\n"

    def notfound(self):
        status = '404 Not Found'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8')]
        self.start_response(status, response_headers)
        yield b"Not Found\n"


if __name__ == '__main__':
    httpd = make_server('', 8086, Application)
    httpd.serve_forever()
