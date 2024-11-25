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
    # print(data.decode())
    if data.decode()=='ACK':
        print(f"Received data:{data.decode()}")
    elif data.decode()=='NACK':
       while data.decode() == "NACK":
            print("Received NACK")
            print(f"Resending {message}")
            client_socket.sendall(message.encode())
            time.sleep(2) #just for slowing the process
            data = client_socket.recv(1024)
       print("Received ACK")


print("Connection ended")

# Close the client socket
client_socket.close()
