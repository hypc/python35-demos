'''
network socket
'''
import socket
from threading import Thread
import time
import unittest
from unittest.case import skip


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.HOST = '127.0.0.1'
        self.PORT = 11133

    @classmethod
    def _server_listen(cls, conn, addr):
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(addr, data)
        finally:
            conn.close()

    @classmethod
    def _server_send(cls, conn, addr):
        try:
            while True:
                conn.sendall(str(time.time()).encode())
                time.sleep(5)
        finally:
            conn.close()

    @skip('')
    def test_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            print('Connected by', addr)
            tl = Thread(target=self._server_listen, args=[conn, addr])
            tl.start()
            ts = Thread(target=self._server_send, args=[conn, addr])
            ts.start()

    @classmethod
    def _client_listen(cls, s):
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(data)

    def test_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))

        sl = Thread(target=self._client_listen, args=[client])
        sl.start()
        while True:
            strs = 'Hello %s' % time.time()
            client.sendall(strs.encode())
            time.sleep(3)

        client.close()

if __name__ == '__main__':
    unittest.main()
