class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    
    def insertbeg(self,data):
        node=Node(data)
        if self.head == None:
            self.head=node
        else:
            temp=self.head
            temp.prev=node
            node.next=temp
            self.head=node
    def printLL(self):
        temp=self.head
        Last=None
        while temp is not None:
            #print(temp.data,'-->',end="")
            last=temp
            temp=temp.next
        
        while last is not None:
            print(last.data,"-->",end=" ")
            last=last.prev    
             
            
                    
            
        
L=DLL()
L.insertbeg(10)
L.insertbeg(20)
L.insertbeg(30)
L.insertbeg(40)
L.insertbeg(50)
L.printLLbeg()

            
                        
        