n,x=map(int,input().split())
y=x*n
a=y//4
if y%4==0:
    n=a
else:
    n=a+1
print(n)
