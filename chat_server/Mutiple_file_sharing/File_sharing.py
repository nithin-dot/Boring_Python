import socket
import threading
import os

import buffer


HOST = '127.0.0.1'
PORT =55554
# Buffer class
class Buffer:
    def __init__(self,s):
        '''Buffer a pre-created socket.
        '''
        self.sock = s
        self.buffer = b''

    def get_bytes(self,n):
        '''Read exactly n bytes from the buffered socket.
           Return remaining buffer if <n bytes remain and socket closes.
        '''
        while len(self.buffer) < n:
            data = self.sock.recv(1024)
            if not data:
                data = self.buffer
                self.buffer = b''
                return data
            self.buffer += data
        # split off the message bytes from the buffer.
        data,self.buffer = self.buffer[:n],self.buffer[n:]
        return data

    def put_bytes(self,data):
        self.sock.sendall(data)

    def get_utf8(self):
        '''Read a null-terminated UTF8 data string and decode it.
           Return an empty string if the socket closes before receiving a null.
        '''
        while b'\x00' not in self.buffer:
            data = self.sock.recv(1024)
            if not data:
                return ''
            self.buffer += data
        # split off the string from the buffer.
        data,_,self.buffer = self.buffer.partition(b'\x00')
        return data.decode()

    def put_utf8(self,s):
        if '\x00' in s:
            raise ValueError('string contains delimiter(null)')
        self.sock.sendall(s.encode() + b'\x00')
def server():
    try:
        os.mkdir('uploads')
    except FileExistsError:
        pass
    socket.bind(('127.0.0.1', port))
    socket.listen()
    communication_socket, address=socket.accept()
    print("Received connection from ", address[0])
    print('Connection Established. Connected From: ', address[0])
    client = (communication_socket.recv(2048)).decode()
    print(client + ' has connected.')
    communication_socket.send(nickname.encode())
    while True:
        conn, addr = socket.accept()
        print("Got a connection from ", addr)
        connbuf = buffer.Buffer(conn)

        while True:
            hash_type = connbuf.get_utf8()
            if not hash_type:
                break
            print('Decrypt Key: ', hash_type)

            file_name = connbuf.get_utf8()
            if not file_name:
                break
            file_name = os.path.join('uploads',file_name)
            print('file name: ', file_name)

            file_size = int(connbuf.get_utf8())
            print('file size: ', file_size )

            with open(file_name, 'wb') as f:
                remaining = file_size
                while remaining:
                    chunk_size = 4096 if remaining >= 4096 else remaining
                    chunk = connbuf.get_bytes(chunk_size)
                    if not chunk: break
                    f.write(chunk)
                    remaining -= len(chunk)
                if remaining:
                    print('File incomplete.  Missing',remaining,'bytes.')
                else:
                    print('File received successfully.')
        print('Connection closed.')
        conn.close()

def client():
    socket.connect(('127.0.0.1', port))
    socket.send(nickname.encode())
    server_name = socket.recv(2048)
    server_name = server_name.decode()
    print(server_name,' has joined...')
    arr_files=[]
    with socket:
        sbuf = Buffer(socket)

    hash_type = input('Enter  Encrpyt Key: ')
    while True:
        files = input('Enter File to Update: ')
        if files=='e':
            break
        arr_files.append(files)

    for file_name in arr_files:
        print(file_name)
        sbuf.put_utf8(hash_type)
        sbuf.put_utf8(file_name)

        file_size = os.path.getsize(file_name)
        sbuf.put_utf8(str(file_size))

        with open(file_name, 'rb') as f:
            sbuf.put_bytes(f.read())
            print('File Sent')

if __name__=="__main__":
    host=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    port=55578
    SIZE = 1024
    FORMAT = "utf-8"
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    choosetype=input("Are you Reciver : ")
    nickname=input("Enter your Nick Name: ")
    print("\nNote: It is a half-duplex communication")
    print("To skip the chat use /e")
    print("Chat only when see Me: in your Terminal\n")
    if choosetype =="yes":      
        server()
    elif choosetype=="no":
        client()
    else:
        print("Please Enter yes or no")