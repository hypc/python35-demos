from http.server import BaseHTTPRequestHandler, HTTPServer


class Hanlder(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))
        print(datas)


if __name__ == '__main__':
    server = HTTPServer(('', 6000), Hanlder)
    server.serve_forever()
