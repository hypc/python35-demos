import re
import traceback
from wsgiref.simple_server import make_server


class wsgiapp(object):

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        self.status = "200 OK"
        self._headers = []

    def header(self, name, value):
        self._headers.append((name, value))

    def __iter__(self):
        try:
            x = self.delegate()
            self.start_response(self.status, self._headers)
        except:
            headers = [('Content-Type', 'text/plain; charset=utf-8')]
            self.start_response("500 Internal Error", headers)
            x = "Internal Error:\n\n" + traceback.format_exc()

        if isinstance(x, str):
            return iter([x])
        else:
            return iter(x)

    def delegate(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func(*args)

        return self.notfound()


class Application(wsgiapp):
    urls = [
        ('/', 'index'),
        ('/hello', 'hello'),
        ('/hello/(.+)', 'hello2'),
    ]

    def GET_index(self):
        self.header('Content-Type', 'text/plain; charset=utf-8')
        print(self.environ['QUERY_STRING'])
        yield b"Welcome!\n"

    def POST_index(self):
        self.header('Content-Type', 'text/plain; charset=utf-8')
        content_length = int(self.environ['CONTENT_LENGTH'])
        body = self.environ['wsgi.input'].read(content_length)
        print(body.decode())
        yield b"Welcome!\n"

    def GET_hello(self):
        self.header('Content-Type', 'text/plain; charset=utf-8')
        yield b"Hello world!\n"

    def GET_hello2(self, name):
        self.header('Content-Type', 'text/plain; charset=utf-8')
        yield b"Hello world!\n"
        yield name.encode()

    def notfound(self):
        self.status = '404 Not Found'
        self.header('Content-Type', 'text/plain; charset=utf-8')
        yield b"Not Found\n"


if __name__ == '__main__':
    httpd = make_server('', 8086, Application)
    httpd.serve_forever()
