import socket
import threading 
import os
from tqdm import tqdm

def server() :
    # def iptoint(ip):
    #     h=list(map(int,ip.split(".")))
    #     return (h[0]<<24)+(h[1]<<16)+(h[2]<<8)+(h[3]<<0)
    # print(f'Share This ShareAddress to Sender :{iptoint(host)}')
    socket.bind(('127.0.0.1', port))
    socket.listen()
    communication_socket, address=socket.accept()
    print("Received connection from ", address[0])
    print('Connection Established. Connected From: ', address[0])
 
    client = (communication_socket.recv(2048)).decode()
    print(client + ' has connected.')
 
    communication_socket.send(nickname.encode())
    # communication_socket.send('NICK'.encode('ascii'))

    def recv():
        while True:
            message_to_client=input('Me :')
            communication_socket.send(message_to_client.encode())
            # print("msg sent")
            msg_server=message_from_client= communication_socket.recv(2048).decode()
            if msg_server == '/e' :
                communication_socket.send(''.encode())
            else: 
                print(client,':', message_from_client)
       
        # communication_socket.close()
        # print(f"connection with {address} ended!")
        # exit(0)
    thread = threading.Thread(target=recv)
    thread.start()



def client():
    # def inttoip(ip):
    #    return ".".join(map(str,[((ip>>24)&0xff),((ip>>16)&0xff),((ip>>8)&0xff),((ip>>0)&0xff)]))
    # otp=int(input("Enter the ShareAddress Recived From Reciver : "))
    socket.connect(('127.0.0.1', port))
    socket.send(nickname.encode())
    server_name = socket.recv(2048)
    server_name = server_name.decode()
    print(server_name,' has joined...')
    def fileshare():
        data = f"{FILENAME}_{FILESIZE}"
        client.send(data.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"SERVER: {msg}")

        """ Data transfer. """
        bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

        with open(FILENAME, "r") as f:
            while True:
                data = f.read(SIZE)

                if not data:
                    break

                client.send(data.encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                bar.update(len(data))
    while True:
            msg_cli = message = socket.recv(2048).decode()
            if  msg_cli =='/e' :
               socket.send(''.encode())
            elif msg_cli == '/help':
                print("You need help right!!")
            else:
                print(server_name, ":", message)
            
            message = input("Me : ")
            socket.send(message.encode())



if __name__=="__main__":
    host=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    port=55578
    SIZE = 1024
    FORMAT = "utf-8"
    FILENAME = "friends-final.txt"
    FILESIZE = os.path.getsize(FILENAME)
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

# print(iptoint(host))
# print(inttoip(iptoint(host)))