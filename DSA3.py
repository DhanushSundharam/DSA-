class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def deletepos(self,index):
        temp=self.head.next
        prev=self.head
        for i in range(index-1+1):
            temp=temp.next
            prev=prev.next 
        prev.next=temp.next  
        #temp.next=None   
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"--->",end=" ")
            temp=temp.next 
                 
                
L=LL()
node=Node(1)

L.head=node
L.insert(10)

L.insert(20)
L.insert(30)
L.insert(40)
L.deletepos(1)
L.display()                    