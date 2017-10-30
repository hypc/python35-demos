from wsgiref.simple_server import make_server


class Application(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain; charset=utf-8')]
        self.start_response(status, response_headers)
        yield b"Hello world!\n"


if __name__ == '__main__':
    httpd = make_server('', 8086, Application)
    httpd.serve_forever()
