import socket
import time

HOST = '192.168.29.225'
PORT = 5000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
TICK_SPEED = .2

seq_nums = int(input("Enter the number of sequence numbers: "))
window_size = int(input("Enter the window size: "))
time.sleep(1)
s.send(str(seq_nums).encode())
data = [i for i in range(seq_nums)]
ack = 0
while ack < seq_nums:
	end = min(ack + window_size, seq_nums)
	window = data[ack:end]
	for i in range(end - ack):
		print(f"Sending packet {window[i]}")
		s.send(str(window[i]).encode())
		time.sleep(TICK_SPEED)
	ack = s.recv(1024).decode()
	ack = int(ack.split(',')[-1])
	print(f"Received ack {ack}")
	for i in range(ack):
		if window:
			window.pop(0)
		else:
			break
print("All packets sent")
print("Closing connection")
s.send(b'exit')
s.close()