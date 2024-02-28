d={}
n,m=map(int,input().split())
for i in range(n):
    name,ip=map(str,input().split())
    d[name]=ip
for i in range(m):
    a,b=map(str,input().split())
    for i in d:
        if d[i]==b[:-1]:
            print(f"{a} {b} #{i}")
         
    
