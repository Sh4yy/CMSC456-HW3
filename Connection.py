import socket

HOST = '128.8.130.16'
PORT = 49106

class Connection:

    def __init__(self, host, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = host
        self._port = port

    def connect(self):
        """ connect to the server """
        self._sock.connect((self._host, self._port))

    def close(self):
        """ close connection """
        self._sock.close()

    def encrypt(self, text, block_size):
        """ send message to be encrypted """
        req = bytearray(str.encode(text))
        req.insert(0, block_size)
        self._sock.sendall(bytes(req))
        resp = self._sock.recv(82)
        return resp[1:16*(block_size+1)+1].hex()

conn = Connection(HOST, PORT)
conn.connect()
result = conn.encrypt("hi there, this is a test", block_size=3)
print(result)
conn.close()
