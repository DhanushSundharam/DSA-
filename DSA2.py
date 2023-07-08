class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    
    def __init__(self):
        self.head=None  
    def display(self):
        
        temp=self.head
        size=0
        while temp:
            
            #print(temp.data,"--->",end=" ")
            temp=temp.next  
            size+=1
        bi=size//2
        #print(bi)
        temp1=self.head
        for i in range(bi):
            
            #print(temp.data,"--->",end=" ")
            temp1=temp1.next  
        
        while temp1:
            print(temp1.data,"-->",end=" ")
            temp1=temp1.next  
                
        
            
                 
        
        
L=LL()
node1=Node(10)
L.head=node1
node2=Node(20)
node1.next=node2
node3=Node(30) 
node2.next=node3
node4=Node(40)
node3.next=node4
node5=Node(50) 
node4.next=node5
L.display()   
