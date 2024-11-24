import time
import random

total_frames=int(input("Enter number of frames:"))
window_size=total_frames//2

ack=[False]*total_frames
sent=[False]*total_frames

ack_received=0
frames_send=0

while ack_received<total_frames:
    for i in range(frames_send,min(frames_send+window_size,total_frames)):
        if not sent[i]:
            print(f"Sending packets :{i}")
            sent[i]=True
            time.sleep(1)

    for i in range(frames_send,min(frames_send+window_size,total_frames)):
        if sent[i] and not ack[i]:
            if random.random()>0.7:
                print(f"Packets deleted:{i}")
                sent[i]=False
                time.sleep(1)
            
            else:
                
                print(f"Acknowledgement received:{i}")
                ack_received+=1
                ack[i]=True
                time.sleep(1)

    while frames_send<total_frames and sent[frames_send]:
        frames_send+=1



