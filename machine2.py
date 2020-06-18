Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> port = 50005
>>> sock.connect(('192.168.1.8', port))
>>> msg = sock.recv(1024)
>>> msg
b'Hello, Thanks For Connecting!'
>>> msg+decoded = msg.decode('utf-8')
SyntaxError: cannot assign to operator
>>> msg_decoded = msg.decode('utf-8')
>>> msg_decoded
'Hello, Thanks For Connecting!'
>>> print('Message from server : ', +msg_decoded)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('Message from server : ', +msg_decoded)
TypeError: bad operand type for unary +: 'str'
>>> print('Message from server : ', msg_decoded)
Message from server :  Hello, Thanks For Connecting!
>>> msg_back = input('Do you want to Responsd To Server ?')
Do you want to Responsd To Server ?Yes, Thank you for Letting me Connect!
>>> msg_back_encoded = msg_back.encode('utf-8')
>>> sock.send(msg_back_encoded)
38
>>> 