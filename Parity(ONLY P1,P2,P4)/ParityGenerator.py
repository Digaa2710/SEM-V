def forOdd(sum):
    if sum%2==1:
        return 0
    return 1

def forEven(sum):
    if sum%2==1:
        return 1
    return 0

def parity_generator():
    if n==0:
        sum=sequence[4]+sequence[2]+sequence[0]#for P1
        sequence[6]=forOdd(sum)
        sum=sequence[4]+sequence[1]+sequence[0]#for P2
        sequence[5]=forOdd(sum)
        sum=sequence[2]+sequence[1]+sequence[0]#for P4
        sequence[3]=forOdd(sum)
    else:
        sum=sequence[4]+sequence[2]+sequence[0]#for P1
        sequence[6]=forEven(sum)
        sum=sequence[4]+sequence[1]+sequence[0]#for P2
        sequence[5]=forEven(sum)
        sum=sequence[2]+sequence[1]+sequence[0]#for P4
        sequence[3]=forEven(sum)
    

print("Choose 0 for odd and 1 for even")
n=int(input("Enter odd or even:"))
data=input("Enter data:")
sequence=[0]*7

sequence[0]=int(data[0])
sequence[1]=int(data[1])
sequence[2]=int(data[2])
sequence[4]=int(data[3])

parity_generator()
print(f"Generated sequence is :{sequence}")



