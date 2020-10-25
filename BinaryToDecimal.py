isByte = False

while isByte == False:
    byte = str(input("\nPlease a byte to convert: "))

    if len(byte) == 8:
        isByte = True
    else:
        print("\nPlease enter a byte, a byte is 8 numbers long")

binarypos = int(128)
number = 0
for each in byte:
    number = number + int(each) * int(binarypos)
    binarypos = binarypos / 2

print(f"\nThe result is {number}")
