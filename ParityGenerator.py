def generate(final,check,parity):
    count=0
    for i in range(len(final)):
        if (len(final)-i) & check:
            count+=int(final[i])
    if parity==0:
        if count%2==0:
            return 0
        else:
            return 1
    elif parity==1:
        if count%2==0:
            return 1
        else:
            return 0
data=input("Enter data:")
n=len(data)
if n==4:
    total_parity=3
elif n==5:
    total_parity=4

parity=int(input("Enter parity:"))
parityPos=[2**i for i in range(total_parity)]
final=['0']*(len(data)+total_parity)
j=1     
for i in range(1,len(final)+1):
    if i in parityPos:
        continue
    final[-i]=data[-j]
    j+=1

for i in range(total_parity):
    final[-parityPos[i]]=str(generate(final,parityPos[i],parity))

print(final)
