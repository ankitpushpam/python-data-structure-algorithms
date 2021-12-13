class Node:
    def __init__(self,name):
        self.children = []
        self.name = name

    def addchild(self,name):
        self.children.append(Node(name))
        return self

graph = Node("A")
graph.addchild("B").addchild("C").addchild("D")
graph.children[0].addchild("E").addchild("F")
graph.children[2].addchild("G").addchild("H")
graph.children[0].children[1].addchild("I").addchild("J")
graph.children[2].children[0].addchild("K")

graph2 = Node("A")
graph2.addchild("B")
graph2.children[0].addchild("C")
graph2.children[0].children[0].addchild("D").addchild("E")
graph2.children[0].children[0].children[0].addchild("F")