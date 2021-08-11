import socket
from termcolor import colored

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
host= "26.22.4.224"
def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!] port %d is closed"%(port),'red'))
    else:
         print(colored("[*] port %d is open"%(port),'green'))

for port in range(134,10000):
    portscanner(port)