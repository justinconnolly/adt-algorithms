class BST:
    class Node:
        def __init__(self, value):
            self.parent = None
            self.left = None
            self.right = None
            self.value = value
        
        def __repr__(self):
            return f"{self.value}"

    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        pass

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node, end=", ")
            self.inOrder(node.right)

    def preOrder(self, node):
        if node is not None:
            print(node, end=", ")
            self.inOrder(node.left)
            self.inOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(node, end=", ")
    

    def add(self, value) -> bool:
        if self.root is None:
            self.root = self.Node(value)
            return True
        curr = self.root
        while curr is not None:
            parent = curr
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return False
        if value < parent.value:
            parent.left = self.Node(value)
            parent.left.parent = parent
        else:
            parent.right = self.Node(value)
            parent.right.parent = parent
        
        return True


    def findPred(self, value) -> Node:
        curr = self.root
        if curr.value == value:
            return curr
        while curr is not None:
            parent = curr
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return parent

    def contains(self, value) -> bool:
        parent = self.findPred(value)
        if parent.value == value:
            return True
        if value < parent.value:
            return parent.left is None
        if value > parent.value:
            return not parent.right is None

    def BFS(self, value):
        distance = -1
        if self.root.value == value:
            return distance + 1
        seen = set()
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            i = queue.pop(0)
            if i is not None and not seen.add(i.right):
                queue.append(i.right)
            if i is not None and not seen.add(i.left):
                queue.append(i.left)
            if i is not None and i.value == value:
                break
        while i is not None:
            distance += 1
            i = i.parent
        return distance


    
if __name__ == "__main__":
    from random import randint
    x = BST()

    x.add(5)
    for i in range(10):
        added = x.add(i)
        print(f"{added}: {i}")

    x.inOrder(x.root)
    print(x.contains(0))
    x.preOrder(x.root)
    print()
    x.postOrder(x.root)
    print()
    x.preOrder(x.root)
    print()
    print(x.BFS(7))
        