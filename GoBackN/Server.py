import socket 
import time
import random

HOST='0.0.0.0'
PORT=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn,addr=s.accept()
TICK_SPEED=0.2

seq_nums=conn.recv(1024).decode()
seq_nums=int(seq_nums)
ack=0
curr=0

while ack<seq_nums:
    received=conn.recv(1024).decode()
    if received=='exit':
        break
    received=int(received)
    print(f"Received:{received}")
    if random.choice([True,False]) and curr==ack:
        curr+=1
        ack=curr
        print(f"Sending ack:{received}")
        conn.sendall((',' + str(ack)).encode())
    else:
        print("Paket failed to send")
    time.sleep(TICK_SPEED)
print("Packets received")
print("Connection ended")
conn.close()