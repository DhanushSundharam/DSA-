class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
    def insertbeg(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def insertend(self,data):
        node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next 
        temp.next=node    
    def removeduplicate(self):
        node=self.head
        while node.next==None:
            if node.value==node.next.value:
                node.next=node.next.next 
            else:
                node=node.next 
                        
                
    def Print(self):
        count=0
        temp=self.head
        if temp==None:
            print("Linked list has been Empty")
        else:
            while temp:
                print(temp.data,"--->",end="")
                temp=temp.next 
                count+=1
    
    def Print1(self):
        count=0
        node=self.head
        if node==None:
            print("Linked list has been Empty")
        else:
            while node:
                print(node.data,"--->",end="")
                node=node.next 
                count+=1
                    
        

L=LL()
L.insertbeg(50)
L.insertbeg(40)
L.insertbeg(30)
L.insertbeg(10)
L.insertbeg(10)
L.insertend(100)
#L.removeduplicate()
L.Print1()
                