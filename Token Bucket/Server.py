import socket
import time
import threading

HOST='0.0.0.0'
PORT=5000

MAX_SIZE=5

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))

server_socket.listen()
conn,addr=server_socket.accept()

tokens=[]
received_data=[]

def leaky():
    while True:
        time.sleep(3)
        if received_data:
            removed_data=received_data.pop(0)
            print(f"Removed data :{removed_data}")
        else:
            print("Bucket is empty")

def handleTokens():
    while True:
        if len(tokens)<MAX_SIZE:
            tokens.append('*')
            print(f"Token bucket looks like :{tokens}")
        else:
            print("Token bucket is full")
        time.sleep(1)

def handleData():
    with conn:
        while True:
            data=conn.recv(1024).decode()
            if not data or data=='end':
                if len(tokens)>0:
                    print(f"Tokens left:{tokens}")
                print("Connection ended by client")
                break

            if len(tokens)>0:
                tokens.pop(0)
                print(f"Data:{data} added to bucket")
                conn.send(data.encode())
                received_data.append(data)
                print(f"Bucket contains:{received_data}")

            else:
                print("No tokens discarding data")
                message="No tokens available"
                conn.send(message.encode())

token_thread=threading.Thread(target=handleTokens,daemon=True)
token_thread.start()

leaky_thread=threading.Thread(target=leaky,daemon=True)
leaky_thread.start()

handleData()

server_socket.close()

