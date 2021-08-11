import socket
s = socket.socket()
socket.setdefaulttimeout(5)
s.connect(("26.22.4.224",21))
ans = s.recv(1024)
print(ans)