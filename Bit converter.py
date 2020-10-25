#setting variables
x = 0
count = 0
binary = ""

#Objects for binary list
class binaryBit:
  def __init__(self, decimal, binary):
    self.decimal = decimal
    self.binary = binary

bit128 = binaryBit(128,0)
bit64 = binaryBit(64,0)
bit32 = binaryBit(32,0)
bit16 = binaryBit(16,0)
bit8 = binaryBit(8,0)
bit4 = binaryBit(4,0)
bit2 = binaryBit(2,0)
bit1 = binaryBit(1,0)

#binary list, I've placed it in this order because it makes calculations easier
decimals = [bit1,bit2,bit4,bit8,bit16,bit32,bit64,bit128]

#user input for conversion
num = int(input("Please enter a number between 0 and 255: "))

#setting user input to a string which will be modified
x = num

#calculating each bit for the binary output
for i in decimals:
    if x % 2 > 0:
        x = (x -1)/2
        decimals[count].binary = 1
        count = count +1
    else:
        x = x / 2
        count = count + 1
    if x < 1:
        break

#taking the binary part of each bit object and appending it to a string for one byte
count = 7
for i in range(8):
    binary = binary + str(decimals[count].binary)
    count = count - 1

#printing result
print("\n{} is {} in binary\n".format(num, binary))

#printing an easily readable table to show what the binary means
count = 7
for i in range(8):
    print(f"{decimals[count].decimal}:\t{decimals[count].binary}")
    count = count - 1

#adding spacing
print("\n")