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
        time.sleep(2)
        
        
        if received_data == "end":
            print("Client has ended communication")
            break

        if random.choice([True,False]):
            print(f"Message received:{received_data}")
            send_message = "ACK"
        else:
            print("Packet lost")
            send_message='NACK'
        print(f"Sending {send_message}")
        conn.sendall(send_message.encode())
    
    conn.close()  

generate_ACK(conn)

server_socket.close() 