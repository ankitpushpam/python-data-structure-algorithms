"""
Breadth First Search

Complexity: O(V+E) Time | O(V) Space - V is vertex and E is edges of the graph

1. First create a queue(using list) and add the first node.
2. While the lenght of the queue is greater than 0, pop a value from the queue and add it to the array.
3. Make a variable current and save the popped value from the queue in the variable current.
4. Add the current value node name (current.name) to the array.
5. And, loop through it's children and add the children(current.children) to the queue.
6. Repeat the step 2 and onwards till the time the queue lenght is zero(it means that there is no node and children left to in the queue)
7. Return the array
"""

class Node:
    def __init__(self,name):
        self.children = []
        self.name = name

    def addchild(self,name):
        self.children.append(Node(self.name))

    def breadthFirstSearch(array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.apppend(child)
        return array
