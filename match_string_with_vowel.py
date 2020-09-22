#get occurance index matcxh with vowels

def getCountWithIndexOfVowels(list_string, vowels):
    elemdic = dict()
    index = 0
    #elemdic = {x:list_string.index(x) for x in list_string if x in vowels}
    for x in list_string:
        if x in vowels:
            if x in elemdic:
                elemdic[x].append(index)
            else:
                #print(x)
                elemdic[x] = [index]
                print(elemdic)
        index +=1
    return elemdic



string = "mehmooth fathima"
vowels = ['a', 'e', 'i', 'o', 'u']
list_string = list(string)
output = getCountWithIndexOfVowels(list_string, vowels)
print(output)

#other method for converting to string to list
#list_string = []
#list_string[:] = string
#print(list_string)
