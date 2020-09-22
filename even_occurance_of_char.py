#input="aabbcccdddd"
#output= "aabbdddd"

input="aabbcccdddd"
length= len(input)
new_string = ""
for i in input:
    if ((input.count(i))%2 == 0):
        new_string = new_string+"".join(i)
print(new_string)


#other method
#char = [i for i in input if (input.count(i))%2 == 0]
#new_string = "".join(char)
#print(new_string)
