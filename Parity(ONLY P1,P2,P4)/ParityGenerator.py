def forOdd(sum):
    if sum % 2 == 1:
        return 0
    return 1

def forEven(sum):
    if sum % 2 == 1:
        return 1
    return 0

def parity_generator():
    if n == 0:  # Odd parity
        if count == 4:  # For 4-bit input
            sum = sequence[4] + sequence[2] + sequence[0]  # For P1
            sequence[6] = forOdd(sum)
            sum = sequence[4] + sequence[1] + sequence[0]  # For P2
            sequence[5] = forOdd(sum)
            sum = sequence[2] + sequence[1] + sequence[0]  # For P4
            sequence[3] = forOdd(sum)
        else:  # For 5-bit input
            sum = sequence[0] + sequence[2] + sequence[4] + sequence[6]  # For P1
            sequence[8] = forOdd(sum)
            sum = sequence[6] + sequence[3] + sequence[2]  # For P2
            sequence[7] = forOdd(sum)
            sum = sequence[4] + sequence[3] + sequence[2]  # For P4
            sequence[5] = forOdd(sum)
            sum = sequence[0]  # For P8
            sequence[1] = forOdd(sum)
    else:  # Even parity
        if count == 4:  # For 4-bit input
            sum = sequence[4] + sequence[2] + sequence[0]  # For P1
            sequence[6] = forEven(sum)
            sum = sequence[4] + sequence[1] + sequence[0]  # For P2
            sequence[5] = forEven(sum)
            sum = sequence[2] + sequence[1] + sequence[0]  # For P4
            sequence[3] = forEven(sum)
        else:  # For 5-bit input
            sum = sequence[0] + sequence[2] + sequence[4] + sequence[6]  # For P1
            sequence[8] = forEven(sum)
            sum = sequence[6] + sequence[3] + sequence[2]  # For P2
            sequence[7] = forEven(sum)
            sum = sequence[4] + sequence[3] + sequence[2]  # For P4
            sequence[5] = forEven(sum)
            sum = sequence[0]  # For P8
            sequence[1] = forEven(sum)

print("Choose 0 for odd and 1 for even")
n = int(input("Enter 0 for odd parity or 1 for even parity: "))
data = input("Enter data:")

count = len(data)
print(f"Input data length: {count}")

if count == 5:
    sequence = [0] * 9
elif count == 4:
    sequence = [0] * 7
else:
    print("Error: Data must be 4 or 5 bits!")
    exit()

sequence[0] = int(data[0])
sequence[1] = int(data[1])
sequence[2] = int(data[2])
sequence[4] = int(data[3])

if count == 5:
    sequence[6] = int(data[4])

parity_generator()

print(f"Generated sequence is: {sequence}")
