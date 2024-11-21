import socket

HOST = '192.168.29.225' 
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    message=input("Enter data:")
    client_socket.sendall(message.encode())
    if(message=="end"):
        break
print("End")
# Close the client socket
client_socket.close()
