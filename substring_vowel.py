#input = "mehmooth fathima"
#vowel = ['a','e','i','o','u']
#output = [['a',[10,15)]], 'e',(1), 'i',(13), o,(4,5)]

input = "mehmooth fathima"
vowel = ['a','e','i','o','u']
out = [[val,key] for key,val in enumerate(input)]
print(out)
print(type(out))
final=[]
for x in out:
#fin_out = {x[0]:(x[0].append(x[1])) for x in out if x[0] in vowel}
    for i in x:
        if i in vowel:
           final.append((i,x[1]))
fin_out = final
dic={}
list1=[]
print(fin_out)
for i,j in enumerate(fin_out):
    print(i,j)
    dic = {x:y for x,y in j if x not in list1}
    print(dic)
    
