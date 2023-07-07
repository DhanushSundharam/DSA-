class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        
    
class LL(object):
    def __init__(self):
        self.head=None
    def insertbeg(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    
    def insertend(self,data):
        node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node   
     
    def insertatpos(self,value,index):
        node=Node(value)
        temp=self.head
        for i in range(index):
            temp=temp.next
        print(temp.next)    
        node.next=temp.next 
        temp.next=node   
    
    def inserdel(self):
        temp=self.head
        self.head=temp.next
        #temp.next=None 
             
        
            
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"--->",end=" ")
            temp=temp.next    
    
L=LL()
node1=Node(10)
L.head=node1
node2=Node(20)
node1.next=node2
node3=Node(30)
node2.next=node3
L.insertbeg(5)
L.insertend(200)
L.insertatpos(471,2)
L.inserdel()
L.display()
