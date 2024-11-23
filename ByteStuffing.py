header=list(input("Enter data header:"))
tail=list(input("Enter data tail:"))
data=list(input("Enter data:"))

i=0
j=0
while i<len(data):
    if(i<len(header) or tail[j]==data[i]):
        data.insert(i,'[$]')
        i+=1
    i+=1
    j+=1
final_data=header+data+tail
print(f"Final result:{final_data}")