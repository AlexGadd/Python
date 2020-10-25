isByte = False
numlist = []
sep = "."
output = ""

userinput = str(input("please enter a binary of an IP: "))
numlist = userinput.split(".")

for each in numlist:
    binarypos = int(128)
    number = 0
    byte = str(each)
    for each in byte:
        number = number + int(each) * int(binarypos)
        binarypos = binarypos / 2
    output = output + str(number) + sep

output = output[:-1]
print(output)
