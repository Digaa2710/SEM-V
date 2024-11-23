frame = [] 
n = int(input("Enter number of frames: "))

for i in range(n):
    frames = input("Enter frame value: ")
    frame.append(frames)

print("Original frames:", frame)

updated_frames = []  
for i in range(len(frame)):
    count = len(frame[i])  
    finish = count + 1 
    updated_frames.append(str(finish))  
    updated_frames.append(frame[i])  

print("Updated frames:", updated_frames)
