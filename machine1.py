Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
>>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol=0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol=0)
TypeError: __init__() got an unexpected keyword argument 'protocol'
>>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> s.bind(('192.168.1.8', 50005))
>>> s.listen(5)
>>> clientsocket,clientaddress = s.accept()
>>> print(clientsocket)
<socket.socket fd=1008, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.8', 50005), raddr=('192.168.1.8', 50423)>
>>> clientaddress
('192.168.1.8', 50423)
>>> print('Got a Connection from %s ' %str(clientaddress))
Got a Connection from ('192.168.1.8', 50423) 
>>> msg = input('Enter Any Message: ')
Enter Any Message: Hello, Thanks For Connecting!
>>> msg_encoded = msg.encode('utf-8')
>>> clientsocket.send(msg_encoded)
29
>>> clientsocket.recv(1024)
b'Yes, Thank you for Letting me Connect!'
>>> message_back = clientsocket.recv(1024)
message_back_decoded = message_back.decode('utf-8')
print('Response From the client : '+ message_back_Decoded)
