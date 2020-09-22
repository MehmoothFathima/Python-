#l1=['apple','orange','mango']
#l2=['apple','orange','mango','orange','apple','mango','apple']
#output=['0,1,2,1,0,2,0]

l1=['apple','orange','mango']
l2=['apple','orange','mango','orange','apple','mango','apple']
"""
output=[]
for ind, val in enumerate(l2):
    if val in l1:
        output.append(l1.index(val))
output1=output
print (output1)
"""
elem = {k: i for i, k in enumerate(l1)}
print(elem)
output = list(map(elem.get, l2))
print(output)
