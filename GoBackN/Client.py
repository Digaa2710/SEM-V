import socket
import time

HOST = '192.168.29.225'
PORT = 5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

TICK_SPEED=0.2

seq_nums=int(input("Enter number of sequences:"))
window_size=int(input("Enter window size:"))

s.send(str(seq_nums).encode())


ack=0
data=[i for i in range(seq_nums)]
while ack<seq_nums:
    end=min(ack+window_size,seq_nums)
    window = data[ack:end]
    for i in range(end-ack):
        print(f"Send data: {window[i]}")
        s.send(str(window[i]).encode())
        time.sleep(TICK_SPEED)
    ack=s.recv(1024).decode()
    ack=int(ack.split(",")[-1])
    print(f"Recieved {ack}")
    for i in range (ack):
        if window:
            window.pop(0)
        else:
            break
print("All packets transferred")
print("Connection ended")
s.close()
