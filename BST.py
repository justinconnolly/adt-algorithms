class BST:
    class Node:
        def __init__(self, value):
            self.parent = None
            self.left = None
            self.right = None
            self.value = value
        
        def __repr__(self):
            return f"{self.value}"
    root = None
    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        if not self.root:
            return "Empty"
        return f"{self.root.value}"

    def inOrderHelper(self, node: Node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node, end=", ")
            self.inOrderHelper(node.right)

    def inOrder(self):
        self.inOrderHelper(self.root)
        print("End")

    def preOrderHelper(self, node: Node):
        if node is not None:
            print(node, end=", ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    def preOrder(self):
        self.preOrderHelper(self.root)
        print("End")

    def postOrderHelper(self, node: Node):
        if node is not None:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            print(node, end=", ")

    def postOrder(self):
        self.postOrderHelper(self.root)
        print("End")
    

    def add(self, value: int) -> bool:
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


    def findPred(self, value: int) -> Node:
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


    def contains(self, value: int) -> bool:
        parent = self.findPred(value)
        if parent.value == value:
            return True
        if value < parent.value:
            return parent.left is None
        if value > parent.value:
            return not parent.right is None

    def BFS(self, value: int):
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


    def findMin(self, node: Node) -> Node:
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def findMax(self, node: Node) -> Node:
        curr = node
        while curr.right is not None:
            curr = curr.right
        return curr


    # this needs to be entirely redone -- the conditionals don't work for 2 child nodes
    def chop(self, child: Node, parent: Node):
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
                

    # this could be MUCH more elegant and less repetitive with a helper
    def delete(self, value: int):
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
                
    
    def setup(self, num):
        from random import randint
        collection = [randint(1,30) for x in range(randint(10, 20))]
        for i in collection:
            self.add(collection.pop())

    # Each leaf is a string sum of the nodes leading from the root to the leaf. Sum all of the leaves.
    def leafStrSum(self):
        curr = self.root
        seen = {}
        stack = [curr]
        sum = []
        seen[self.root.value] = str(self.root.value)
        while stack:
            i = stack.pop()
            if i.left and i.left not in seen:
                seen[i.left.value] = seen[i.value] + str(i.left.value)
                stack.append(i.left)
            if i.right and i.right not in seen:
                seen[i.right.value] = seen[i.value] + str(i.right.value)
                stack.append(i.right)
            if not i.left and not i.right:
                sum.append(seen[i.value])
        for key in seen.keys():
            print(f"{key.value}: {seen[key]}")
        retSum = 0
        for num in sum:
            retSum += int(num)
        return retSum

    def traverse2(self):
        path = [None]#[self.root]
        prev = None
        curr = self.root
        sumList = []
        # visited = []
        seen = {}
        while curr:
            print(curr.value)
            if not curr.left and not curr.right:
                sumList.append(path)
            if prev is path[len(path) - 1]:
                path.append(curr)
            if curr.left and prev is not curr.left:
                prev = curr
                curr = curr.left
            elif curr.right and prev is not curr.right:
                prev = curr
                curr = curr.right
            else:
                curr = prev
        print(path)
        path.pop(0)
        import functools
        print(functools.reduce(lambda a, b: str(a) + str(b), [x.value for x in path]))
        print(sumList)


    def traverseAndLeetcodeOneTwoNine(self):
        curr = self.root
        prev = None
        next = None
        path = [None]
        leafSum = []
        while curr:
            if prev is path[len(path) - 1]:
                if curr.left:
                    next = curr.left
                    path.append(curr)
                elif curr.right:
                    next = curr.right
                    path.append(curr)
                else:
                    leafSum.append(path[1:])
                    leafSum[len(leafSum) - 1].append(curr.value)
                    # print(f"Path: {path}")
                    # print(f"Leaf! {curr.value}")
                    next = path.pop()
            elif curr.left and prev is curr.left:
                if curr.right:
                    next = curr.right
                    path.append(curr)
                else:
                    next = path.pop()
            else:
                next = path.pop()
            prev = curr
            curr = next
        # print(leafSum)
        # import functools
        # print(functools.reduce(lambda a, b: str(a) + str(b), [x.value for x in y]) for y in leafSum)

        sum = 0
        eq = ""
        for valList in leafSum:
            strSum = ""
            for value in valList:
                strSum += str(value)
            sum += int(strSum)
            eq += strSum + " + "
        #     print(strSum)
        eq = eq[:-3]
        eq += " = " + str(sum)
        print(eq)
        return sum





    
if __name__ == "__main__":
    # from random import randint
    # x = BST()

    # x.add(5)
    # for i in range(10):
    #     added = x.add(i)
    #     print(f"{added}: {i}")

    # x.inOrder(x.root)
    # print()
    # x.preOrder(x.root)
    # print()
    # x.postOrder(x.root)
    # print()

    x = BST()
    x.add(5)
    x.add(2)
    x.add(3)
    x.add(1)
    x.add(6)
    x.traverseAndLeetcodeOneTwoNine()