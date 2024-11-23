data=list(input("Enter data"))
counter=0
i=0
while i<len(data):
    if data[i]=='1':
        counter+=1
    else :
        counter=0
    if counter==5:
        data.insert(i+1,'0')
        counter=0
    i+=1
print(data)