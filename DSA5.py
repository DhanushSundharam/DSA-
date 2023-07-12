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
                
    def Print(self):
        count=0
        temp=self.head
        if temp==None:
            print("Linked list has been Empty")
        else:
            while temp:
                print(temp.data,end="")
                temp=temp.next 
                count+=1
        """
        mid=count//2
        temp1=self.head
        for i in range(mid):
            #print(temp1.data,"--->",end="")
            temp1=temp1.next                 
        print(temp1.data)   """
                 

L=LL()
L.insertbeg(50)
L.insertbeg(40)
L.insertbeg(30)
L.insertbeg(20)
L.insertbeg(10)
#L.insertend(100)
L.Print()
                