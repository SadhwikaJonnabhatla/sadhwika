class Node:
    def __init__(self,data=0):
        self.data=data
        self.Next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2)
a.insertatbeg(3)
a.insertatbeg(4)
print(a.head.data)
print(a.head.next.data)
print(a.head.next.next.data)
print(a.head.next.next.next.data)



