#input = 2
#str1 = i.like.this.program.very.much
#str2 = pqr.mno

num = int(input("Enter the number of statement"))
print(num)
s_list = []
output =[]
if (num >= 1) and (num <= 100):
    for i in range(num):
        s = input("Enter string")
        if len(s) >= 1 and len(s) <=2000:
            s_list.append(s)
        else:
            print("String out of range")
            break
else:
    print("Not a valid input")
    #break

print(s_list)


def reverse(s_list):
    for x in s_list:
        list = x.split(".")
        print(list)
        list1 = list[::-1]
        str1 = ".".join(list1)
        output.append(str1)
    return (output)

out1 = reverse(s_list)
print(out1)
print('\n'.join([x for x in out1]))
