import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
while True:
    data=str(s.recv(1024)).strip('b').strip('\'')
    print(data)
    m=bytes("Server:"+input(r""),encoding='utf-8')
    s.send(m)