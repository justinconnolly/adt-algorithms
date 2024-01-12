class BST:
    class Node:
        def __init__(self, val: int, parent=None,left=None,right=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.val = val

        def __str__(self):
            return f'{self.val}'

    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return self.str_helper(self.root)

    def str_helper(self, node):
        return f'{f"{self.str_helper(node.left)}, " if node.left else ""}{node.val}{f", {self.str_helper(node.right)}" if node.right else ""}'

        
    def find_pred(self, val: int) -> Node:
        if self.root is None:
            return self.root
        return self.find_pred_helper(self.root,val)

    def find_pred_helper(self, curr: Node, val: int, prev=None) -> Node:
        if curr is None:
            return prev
        if val == curr.val:
            return curr
        if val > curr.val:
            return self.find_pred_helper(curr.right, val, curr)
        if val < curr.val:
            return self.find_pred_helper(curr.left, val, curr)

    def insert(self, val):
        if self.root is None:
            self.root = self.Node(val)
        else:
            parent = self.find_pred(val)
            self.add_child(parent, self.Node(val, parent))

    def add_child(self, parent: Node, child: Node) -> bool:
        if parent is None:
            self.root = parent
        else:
            if child.val < parent.val:
                parent.left = child
                child.parent = parent
            elif child.val > parent.val:
                parent.right = child
                child.parent = parent
            else:
                return False
        self.size += 1
        return True
    
    def find(self, val):
        return self.find_helper(self.root, val)
    
    def find_helper(self, curr, val):
        if curr is None:
            return False
        if curr.val == val:
            return True
        if val > curr.val:
            return self.find_helper(curr.right, val)
        else:
            return self.find_helper(curr.left, val)
        
    def count_nodes_one_child(self, curr):
        if curr is None:
            return 0
        if (curr.left or curr.right) and not (curr.left and curr.right):
            return 1 + self.count_nodes_one_child(curr.left if curr.left else curr.right)
        return self.count_nodes_one_child(curr.left) + self.count_nodes_one_child(curr.right)
    
    def print_tree(self):
        tree = []
        self.print_tree_from_node(self.root, tree)
        for line in tree:
            print(line)
        # print(tree)

    def print_tree_from_node(self, node, tree, padding=''):
        if node:
            tree.append(f'{padding}{node.val}')
            self.print_tree_from_node(node.left, tree, padding + '   ')
            self.print_tree_from_node(node.right, tree, padding + '   ')


def count_nodes_one_child(runs):
    sum = 0
    for _ in range(runs):
        myt = BST()
        elements = [x for x in range(runs)]
        shuffle(elements)
        for j in elements:
            myt.insert(j)
        one_child_nodes = myt.count_nodes_one_child(myt.root)
        sum += one_child_nodes / runs
    print(f'{sum/(runs):.5}')


if __name__ == "__main__":
    from random import shuffle
    runs = 1000
    count_nodes_one_child(runs)
    myt = BST()
    elements = [x for x in range(10)]
    shuffle(elements)
    elements = [5,2,3,8,4,9,7,1,6]
    for i in elements:
        myt.insert(i)
    myt.print_tree()