class Graph:
    def __init__(self):
        self.nodeList = []
    
    def addNode(self, value: int, outEdges: list):
        nodeList.append(Node(value))
        for edge in outEdges:
            nodeList[len(nodeList) - 1].addOut(edge)

# really need to decide how nodes will be referenced -- they probably don't need values for this graph (DFS/BFS), they can be referenced using their position in the graph array
#just use an adjacency list
class Node:
    def __init__(self, value: int):
        self.outEdges = []
        self.value = value

    def addOut(self, newNeighbour: Node):
        self.outEdges.append(newNeighbour)
    
    def removeOut(self, removedNode: Node):
        self.outEdges.remove(removedNode)
    
if __name__ == '__main__':
    from random import randint,choice

    nodeList = [Node(x) for x in range(5)]

    for index, node in enumerate(nodeList):

        outList = list(range(0,len(nodeList)))
        outList.remove(index)

        # this can be simplified with random.sample()
        for i in range(randint(0,len(nodeList))):
            temp = randint(0,len(outList)-1)
            if temp > 0:
                node.addOut(outList.pop(temp))

    for node in nodeList:
        print(node.value, end = ": ")
        print(node.outEdges)
