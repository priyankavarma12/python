#Python Program for tcp server

import socket
from datetime import datetime

HOST =  "192.168.1.8"
PORT = 6789
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print('Starting the server at : ', datetime.now())
print("Waiting For the Incoming Connection From Client.....")

sock.listen(5)
client, addr = sock.accept()

while True:
    data = client.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print("At ", datetime.now(), addr, " said ", data.decode('utf-8'))
    message_to_client = input("Enter Message to Client:  ")
    message_to_client_encoded = message_to_client.encode('utf-8')
    client.send(message_to_client_encoded)
    if message_to_client == 'q':
        break
    
client.close()
s.close()  
    
    
    
    
