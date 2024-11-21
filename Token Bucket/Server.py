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

tokens=[]
incoming_data=[]

token_lock = threading.Lock()

def generate_token():
    
    while True:
        
        with token_lock:
            if len(tokens)<MAX_SIZE:
                tokens.append('*')
            else:
                print("Token bucket is full")
        time.sleep(1/LEAK_RATE)
        
def Data():
     with conn:
        while True:
           
            data = conn.recv(1024)
            if not data or data.decode() == "end":
                if len(tokens)>0:
                    print(f"Remaining data:{incoming_data}")
                print("Client has ended communication")
                break

            with token_lock:
                if len(tokens) != 0:
                    incoming_data.append(data.decode())
                    tokens.pop(0)
                    print(f"Received data: {incoming_data}")
                else:
                    print("Bucket is empty. Discarding new data.")
Token_thread = threading.Thread(target=generate_token, daemon=True)
Token_thread.start()


Data()

# Close the server socket
server_socket.close()