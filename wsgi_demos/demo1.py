from wsgiref.simple_server import make_server, demo_app


if __name__ == '__main__':
    httpd = make_server('', 8086, demo_app)
    httpd.serve_forever()
