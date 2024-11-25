import socket

HOST='192.168.29.225'
PORT=5000

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    message=input("Enter message:")
    client_socket.send(message.encode())
    if message=='end':
        break
print("End")
client_socket.close()