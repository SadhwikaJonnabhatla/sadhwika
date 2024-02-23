r,c=int(input()),int(input())
nl,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)
