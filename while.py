n,m=int(input()),int(input())
i=n
while i <= m:
    if i%6!=0 and i%7!=0 and i%8!=0:
        print(i)
    i+=1
