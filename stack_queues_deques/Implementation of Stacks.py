"""
Implementation of Stacks using Python:
Stack is data structure which is linear in structure and the element which enter the the last will be out first. 
This is also called as Last in First out. It is an ordered collection of item where the addition of the new item
and removal of the existing items always take place at the same end, and that end is usually referred as top. The bottom of the stack is called as base.

Below are the available operation to a stack:
1. Stack() - this will create a new empty stack structure.
2. isempty() - to check whether a stack is empty.It return true if the stack is empty
3. push(item) - it add the item to the top of the stack and return nothing.
4. pop() - it remove the last existing item from the stack or the top item of the stack and return that item.
5. peek() - it return the last existing item from the stack or the top item of the stack but it does not modify the stack.
6. size() - it return the size of the stack
"""

class Stack():

#this function will create a new stack; the stack is implemented using list data structure of python
    def __init(self):
        self.items = []

    def isempty(self):
        return self.items == []  #return true if the stack is empty

    def push(self,item):
        self.items.append(item)  #adding the parameter item at the top of the stack

    def pop(self):
        self.items.pop(len(self.items)-1) #remove the last element existing element from the stack

    def peek(self):
        self.items[len(self.items)-1] #will return the last element from the stack, it does not modify the stack

    def size(self):
        self.len(self.items) #will return the size of the stack




    