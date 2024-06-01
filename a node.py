class Node:
    def __init__(self,data=0):
        self.data=data
        self.Next=None
a=Node(1)
b=Node(2)
c=Node(3)
a.Next=b
b.Next=c
print(a.data)
print(a.Next.data)
print(a.Next.Next.data)
