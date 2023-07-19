class Node:
    def __init__(self,data):
        self.Data=data
        self.Next=None

class LinkedList:
    def __init__(self):
        self.Head=None
    def insertEnd(self,data):
        node=Node(data)
        temp=self.Head
        if temp == None:
            temp=node
        else:
            while temp:
                temp=temp.Next 
            temp.Next=node
            #temp.head.Next=node
    def Print(self):
        temp=self.Head
        while temp :
            print(temp.Data,"-->",end=" ")
            temp=temp.Next        

def BoolenCycle(Lin):
    fast=Lin.Head
    slow=Lin.Head
    while (fast != None) and (fast.next !=None):
        fast=fast.Next.Next
        slow=slow.Next
        if fast==slow:
            temp=slow
            lenght=0
            while fast!=slow :
                temp=slow.next 
                lenght+=1
            return lenght    
    return False+

                
                        

Linked=LinkedList()        
Linked.insertEnd(10) 
Linked.insertEnd(20)  
Linked.insertEnd(30)
Linked.insertEnd(40)
Linked.insertEnd(50)
Linked.Print()
#x=BoolenCycle(Linked)     
#print(x)        