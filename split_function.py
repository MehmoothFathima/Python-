#split function
#input = 001011001100010001112021221111222002111012

input = "001011001100010001112021221111222002111012"
length = len(input)
print(length)
n=2
for i in range(0,length,n):
    print(input[i:i+n])

    #print(i+str(i))
