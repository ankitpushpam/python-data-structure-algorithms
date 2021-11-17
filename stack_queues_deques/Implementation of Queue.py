"""
Implementation of the Queue using Python:
Queue is an ordered collction of items and it is linear in structure. The addition if the item always happens 
at the back/rear of the structure called as rear.And, removal of the item always happens from the front of the structure called as front. 

Below are the available attributes and methods to a Queue.
1. Queue() : It will create a empty queue.
2. isempty() : It will check whether the queue is empty. It will return true if the queue is empty
3. enqueue(item): It will add the item to the rear end of the queue. It return nothing.
4. dequeue(): It will remove the a item from the front of the queue. It return the removed item.
5. size(): It returns the size of the queue. 
"""

class Queue():

    def __init__(self):
        self.items = [] #creating a new queue using the list data structure of python

    def isempty(self):
        return self.items == [] #return true if the queue is empty

    def enqueue(self,item):
        self.items.insert(0,item) #adding the item at the end of the queue

    def dequeue(self):
        return self.items.pop()  #remove the first item from the front of the queue

    def size(self):
        return len(self.items)

q = Queue()

print(q.isempty())
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.isempty())
print(q.dequeue())
print(q.size())
    