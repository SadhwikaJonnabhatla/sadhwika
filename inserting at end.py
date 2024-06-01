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
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.Next
    def insertatend(self,value):
        newnode=Node(value)
        if not self.head:
            self.head=newnode
        else:
            curr=self.head
            while curr.Next:
                curr=curr.Next
            curr.Next=newnode
            
a=linkedlist()
a.insertatbeg(1)
a.insertatbeg(2)
a.insertatbeg(3)
a.insertatbeg(4)
a.insertatend(5)
a.printlist()

