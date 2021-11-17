"""
Implementation of Deque using Python

Deque is very similar to queue along with some extra feature such freedom of adding and 
removing the element from both the end which is front and rear.

Attributes and Methods of Deque:
1. Deque() : It will create an empty deque.
2. isempty() : It will return true if the deque is empty.
3. addfront(item) : It will add the item at the front of the deque.
4. addrear(item) : It will add the item at the rear of the deque.
5. removefront() : It will remove the item from the from of the deque and return the removed item.
6. removerear() : It will remove the item from the end of the deque and return the removed item.
7. size() : It will return the size of the deque.

"""

class Deque():
    
    def __init__(self):
        self.items = []  #creating an empty deque

    def isempty(self):
        return self.items == [] #return true of deque is empty

    def addfront(self,item):
        self.items.append(item)  #adding the item at the end of the deque

    def addrear(self,item):
        self.items.insert(0,item) #adding the item at the front of the deque

    def removefront(self):
        return self.items.pop() #will remove the item from the front of the deque

    def removerear(self):
        return self.items.pop(0)  #will remove the item from the rear of the deque

    def size(self):
        return len(self.items)


d = Deque()

d.addfront('hello')
d.addrear('world')

print(d.size())

print(d.removefront() + ' ' +  d.removerear())
print(d.size())


    

