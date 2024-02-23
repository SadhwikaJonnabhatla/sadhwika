r,c=int(input("rows:")),int(input("colums:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
sumn=0
for i in l:
    print(i)
    sumn+=sum(i)
print(sumn)
