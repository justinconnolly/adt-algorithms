class DoublyLinkedList:

    class Node:
        def __init__(self, value = None):
            self.value = value
            self.next = None
            self.prev = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.length = 0
        self.dummy = self.Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def getNode(self, i):
        p = None
        if (i < self.length / 2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(i,0,-1):
                p = p.prev
        return p

    def get(self, i):
        return self.getNode(i)

    def set(self, i, x):
        u = self.getNode(i)
        y = u.value
        u.value = x
        return y

    def addBefore(self, node, value):
        newNode = self.Node(value)
        newNode.prev = node.prev
        newNode.next = node
        newNode.next.prev = newNode
        newNode.prev.next = newNode
        return newNode

    def size(self):
        return self.length

    def add(self, value, i = None):
        self.length += 1
        if self.length == 0:
            i = 0
        if i is None:
            i = self.length
            # alternatively
            # self.addBefore(self.dummy, value)
            # return
        self.addBefore(self.getNode(i), value)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def remove(self, i):
        w = self.getNode(i)
        self.removeNode(w)
        return w.value

    def print(self):
        node = self.dummy.next
        nodes = []
        i = 0
        while i < self.length:
            i += 1
            nodes.append(str(node.value))
            node = node.next
        nodes.append("End")
        print(" -> ".join(nodes))