#Input : {“Gfg” : [4, 7, 5], “Best” : [8, 6, 7], “is” : [9, 3, 8]}, K = 2
#Output : [5, 7, 8]

from operator import itemgetter
input = {"gfg" : [4, 7, 5], "best" : [8, 6, 7], "abc" : [9, 3, 8]}
k=0
final=[]
for ind,val in enumerate(input.values()):
    print(ind,val)
    final.append(val[k])
print(final)


"""
other method:1
res = list(map(itemgetter(k), input.values()))
print(res)

other method:2
res = [sub[k] for sub in input.values()]
print(res)
"""
