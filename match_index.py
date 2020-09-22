#l1=[2,4,3,5,7]
#l2=[2,4,1,5,6]
#ch1=[2,3,7] out=false
#ch2=[4,5,2]out=True

l1=[2,4,3,5,7]
l2=[2,4,1,5,6]
ch1=[2,3,7]
out=True
for x in ch1:
    if (x in l1 and x in l2) and l1.index(x) == l2.index(x):
            pass
    else:
        out= False
        break
print(out)
