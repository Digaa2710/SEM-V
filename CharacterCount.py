frame=list(input("Enter frames:"))
count=0
for i in range(len(frame)):
    count=count+1
final=count+1
frame.insert(0,final)
print(frame)