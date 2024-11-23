frame=[]
n=int(input("Enter number of frames:"))
for i in range(n):
    frames=int(input("Enter frame value:"))
    frame.append(frames)
print(frame)
count=0
for i in range(len(frame)):
    count=count+1
final=count+1
frame.insert(0,final)
print(frame)