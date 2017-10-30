from wsgiref.simple_server import make_server


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, response_headers)
    return [b'Hello world!\n']


if __name__ == '__main__':
    httpd = make_server('', 8086, application)
    httpd.serve_forever()
