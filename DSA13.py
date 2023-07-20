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
   
    
    def Print1(self):
        if self.head == None:
            return self.head
        prev=None
        present=self.head
        Next=present.next 
        while (present != None):
            present.next=prev
            prev=present
            present=Next 
            if Next!=None:
                Next=Next.next 
          
        count=0
        node=prev
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
L.Print2()  
L.Print1()        