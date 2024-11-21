import socket
import threading
import time

MAX_SIZE = 5 
LEAK_RATE = 0.5
HOST = '0.0.0.0'
PORT = 5001


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))


server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

received_data = []


def leaky():
    while True:
        time.sleep(1 / LEAK_RATE)  
        if received_data:
            leaked_data = received_data.pop(0)  
            print(f"Leaked data: {leaked_data}")
        else:
            print("Bucket is empty, no data to leak.")


def addInQueue():
    with conn:
        while True:
           
            data = conn.recv(1024)
            if not data or data.decode() == "end":
                if len(received_data)>0:
                     print(f"Remaining data: {received_data}")

                print("Client has ended communication")
                break

           
            if len(received_data) < MAX_SIZE:
                received_data.append(data.decode())
                print(f"Received data: {received_data}")
            else:
                print("Queue is full. Discarding new data.")

# Run the leaky bucket function in a separate thread
leaky_thread = threading.Thread(target=leaky, daemon=True)
leaky_thread.start()


addInQueue()

# Close the server socket
server_socket.close()
