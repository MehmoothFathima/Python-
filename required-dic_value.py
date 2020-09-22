#getting dictionary required value by passing list
#input = {'gfg' : [4, 6], 'is' : [10], 'best' : [4, 5, 7]}
#req_list = [4, 6, 10]
#output = {'gfg' : [4, 6], 'is' : [10]}

input = {'gfg' : [4, 6], 'is' : [10], 'best' : [4, 5, 7]}
req_list = [4, 6, 10]
temp=set(req_list)
output=[]
dic_value = {key:set(val) for key, val in input.items()}
print(dic_value)
for x,va in dic_value.items():
    print(x)
    if va.issubset(temp):
        output.append((x,va))
print(output) #to return in list

#one line description
#output = [(key,val) for key, val in dic_value.items() if dic_value[key].issubset(temp)]
#print(output)
"""
#to return in dictionary need to use below step
temp = set(req_list)
print(temp)
temp2 = { key: set(val) for key, val in input.items() }
print(temp2)
    #return { key: val for key, val in test_dict.items() if temp2[key].issubset(temp)} 
"""
