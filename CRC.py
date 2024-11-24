def XOR(a, b):
    if a==b:
        return '0'
    return '1'

def divison(data,generator):
    while len(data) >= len(generator):
    
        for i in range(len(generator)):
            data[i] = XOR(data[i], generator[i])
        print(data)
        while len(data) > 0 and data[0] == '0':
            data.pop(0)
        if len(data)<len(generator)-1:
            i=0
            while len(data)!=len(generator)-1:
                data.insert(i,'0')
                i=i+1
    reminder=''.join(data)
    return reminder

data = list(input("Enter data:"))
generator = list(input("Enter generator:"))
original_data = data.copy()
for i in range(len(generator) - 1):
    data.append('0')

print(f"Data after appending zeros: {data}")
reminder=divison(data,generator)
print(f"Remainder (CRC):{reminder}")
 
dataTransmitted=original_data+list(reminder)
print(''.join(dataTransmitted))

final_result=divison(dataTransmitted,generator)
print(f"Final result:{final_result}")

count=0
for i in range(len(final_result)):
    if(final_result[i]=='0'):
        count=count+1
if count==len(final_result):
    print("No error detected")
else:
    print("Error detected")
    






