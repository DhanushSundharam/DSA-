
    
    
    
    
    
    
    
def findsquare(num):
    ans=0
    while num>0:
        rem=num%10
        ans=ans+(rem*rem)
        num//=10
    
    return ans
 

def ishappy(n):
    slow=n
    fast=n 
    
    while True:
        slow=findsquare(slow)
        fast=findsquare(findsquare(fast))
    
        if slow == fast: 
          break 
        
    if slow==1:
       return True
    else:
        return False    
    
x=ishappy(19)
print(x)      
