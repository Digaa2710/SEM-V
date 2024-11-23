import socket
import time
import random

HOST = '0.0.0.0'
PORT =5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)
TICK_SPEED =0.2
time.sleep(1)
seq_nums = int(conn.recv(1024).decode())
# window_size = 1

ack = 0
curr = 0
while ack < seq_nums:
	received = conn.recv(1024).decode()
	if received == 'exit':
		break
	received = int(received)
	print(f"Received packet {received}")
	if random.choice([True, False]) and received == curr:
		curr += 1
		ack = curr
		print(f'Sending ack {ack}')
		conn.sendall((',' + str(ack)).encode())
	else:
		print(f"Packet lost {received}, Expected {curr}")
		conn.sendall((',' + str(curr)).encode())
	time.sleep(TICK_SPEED)
print("All packets received")
print("Closing connection")
conn.close()