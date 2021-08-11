import socket
socket.setdefaulttimeout(5)
s = socket.socket()
s.connect(("192.168.183.2",135))
print(s.recv(1024))
