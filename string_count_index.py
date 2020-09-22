#finding count with index

def getCountWithIndex(list_string):
    elemdic = dict()
    index = 0
    for x in list_string:
        if x in elemdic:
            elemdic[x][0] +=1
            elemdic[x][1].append(index)
        else:
            elemdic[x] = [1, [index]]
        index +=1
    return elemdic



string = "mehmooth fathima"
list_string = list(string)
print(list_string)
output = getCountWithIndex(list_string)
print(output)
