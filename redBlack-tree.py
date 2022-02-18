class Node:
    value = 0
    colour = 0
    parent = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class redBlackTree:
    root = None
    def __init__(self, value):
        self.root = Node(value)

    def __repr__(self):
        return f"{self.root.value}"

tree = redBlackTree(5)
print(tree)
