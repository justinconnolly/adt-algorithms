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
        while curr is not None and curr.value != value:
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


    def findMin(self, node) -> Node:
        curr = node
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr


    # this needs to be redone -- the conditionals don't work for 2 child nodes
    def chop(self, child, parent):
        if child.value < parent.value:
            if child.left is None and child.right is None:
                parent.left = None
                child.parent = None

            elif child.left is not None or child.right is not None:
                if child.right is not None:
                    parent.left = child.right
                    parent.left.parent = parent
                else:
                    parent.left = child.left
                    parent.left.parent = parent
            else:
                # child.parent = parent.parent
                # child.parent.left = child
                # child.
                replacement = self.findMin(child)
                print(replacement)
                print("ELSE")
                

        else:
            if child.left is None and child.right is None:
                parent.right = None
                child.parent = None

            elif child.left is not None or child.right is not None:
                if child.right is not None:
                    parent.right = child.right
                    parent.right.parent = parent
                else:
                    parent.right = child.right
                    parent.right.parent = parent
            else:
                replacement = self.findMin(child)
                print(replacement)
                print("ELSE")
            print("BOOP")

                

    # this could be MUCH more elegant and less repetitive with a helper
    def delete(self, value):
        if self.contains(value):
            parent = self.findPred(value)
            if value < parent.value:
                node = parent.left
                if node.left is None and node.right is None:
                    parent.left = None
            else:
                node = parent.right
                if node.left is None and node.right is None:
                    parent.right = None
                
                




    
if __name__ == "__main__":
    from random import randint
    x = BST()

    x.add(5)
    for i in range(10):
        added = x.add(i)
        print(f"{added}: {i}")

    x.inOrder(x.root)
    print()
    x.preOrder(x.root)
    print()
    x.postOrder(x.root)
    print()
    # print(x.BFS(7))

    two = x.findPred(2).right
    three = x.findPred(3).right
    print(three)
    four = x.findPred(4).right
    print(four)
    # x.chop(four, three)
    x.chop(three, two)

    x.inOrder(x.root)
    zero = x.findMin(x.root.right)
    print(zero)

    x.chop(x.root.right,x.root)