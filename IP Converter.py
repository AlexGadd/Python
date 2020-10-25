usrInput = ""
numList = []
binIntermediary = ""
binOutput = ""

def stringReverse(x):
  return x[::-1]

usrInput = str(input("\nPlease enter the IP address you would like to convert: "))

numList = usrInput.split(".")

leng = len(numList)

while leng > 0:
    numList[leng - 1] = int(numList[leng - 1])
    leng = leng -1

leng = len(numList)

while leng > 0:
    count = 8
    while count > 0:
        if numList[leng - 1] % 2 > 0:
            numList[leng - 1] = (numList[leng - 1] -1) / 2
            binIntermediary = binIntermediary + "1"
            count = count -1
        else:
            numList[leng - 1] = numList[leng - 1] / 2
            binIntermediary = binIntermediary + "0"
            count = count -1 
    binOutput = binOutput + binIntermediary
    binIntermediary = " "
    leng = leng -1
binOutput = stringReverse(binOutput)

print(f"\n{binOutput}\n")