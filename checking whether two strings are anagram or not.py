s1,s2=map(str,input().split())
c,d=s1.lower(),s2.lower()
a,b=set(c),set(d)
if len(s1)==len(s2):
    if a==b:
        print("True")
    else:
        print("False")
else:
    print("False")
