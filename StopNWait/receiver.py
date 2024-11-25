import socket
import time
import random

HOST = '0.0.0.0'  # Server's IP address
PORT = 5001  # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

def generate_ACK(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_data = data.decode()
        if random.choice([True,False]):
            print(f"Received data: {received_data}")
        time.sleep(2)
        
        
        if received_data == "end":
            print("Client has ended communication")
            break

        send_message = f"ACK for {received_data}"
        conn.sendall(send_message.encode())
    
    conn.close()  

generate_ACK(conn)

server_socket.close() 