class Graph:
    def __init__(self):
        self.nodeList = []
    
    def addNode(self, value):
        pass

class Node:
    def __init__(self, value):
        self.outEdges = []
        self.value = value

    def addOut(self, newNeighbour):
        self.outEdges.append(newNeighbour)
    
    def removeOut(self, removedNode):
        self.outEdges.remove(removedNode)
    
if __name__ == '__main__':
    from random import randint,choice

    nodeList = [Node(x) for x in range(5)]

    for index, node in enumerate(nodeList):

        outList = list(range(0,len(nodeList)))
        outList.remove(index)

        # this can be simplified with random.choice()
        for i in range(randint(0,len(nodeList))):
            temp = randint(0,len(outList)-1)
            if temp > 0:
                node.addOut(outList.pop(temp))

    for node in nodeList:
        print(node.value, end = ": ")
        print(node.outEdges)
