def counting(s):
    print(s)
    s1,vc='',0
    for i in s:
        if i.lower() in"aeiou":
            vc+=1
            s1+=i
    print("vowels count:",vc)
    print(list(set(s1)))
l=input().split()
for i in l:
    counting(i)
