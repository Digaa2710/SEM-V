ip=input("Enter ip address:")
octets=ip.split('.')
subnet='0.0.0.0'
subnet_split=subnet.split('.')
if (int(octets[0])>=0 and int(octets[0])<=127):
    ip_class='A'
    subnet_class=1
elif (int(octets[0])>=128 and int(octets[0])<=191):
    ip_class='B'
    subnet_class=2
elif(int(octets[0])>=192 and int(octets[0])<=223):
    ip_class='C'
    subnet_class=3
elif(int(octets[0])>=224 and int(octets[0])<=239):
    ip_class='D'
    subnet_class=4
else:
    ip_class='E'
    subnet_class=5
print(f"Ip belongs to class:{ip_class}")
for i in range(subnet_class):
    subnet_split[i]='255'
# print(subnet_split)
subnet_mass=('.').join(subnet_split)
print(f"Subnet mass of given class is :{subnet_mass}")

result = [str(int(a) & int(b)) for a, b in zip(octets, subnet_split)]
result_ip = '.'.join(result)

print(f"Result of bitwise AND (Network Address): {result_ip}")
