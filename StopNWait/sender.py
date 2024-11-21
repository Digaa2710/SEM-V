import socket
import time

HOST = '192.168.29.225'  # Server's IP address
PORT = 5001  # Server's port

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter data: ")

    client_socket.sendall(message.encode())
    if message == "end":
        break

    data = client_socket.recv(1024)
    time.sleep(2) #just for slowing the process
    print(data.decode())

print("Connection ended")

# Close the client socket
client_socket.close()
