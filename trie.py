class Trie:
    class Node:
        def __init__(self, value):
            self.children = dict()
            self.end = False
            self.value = value

    def __init__(self):
        self.root = self.Node("*")
    
    def add(self, word:str):
        return self.addHelper(self.root, word)
    
    def addHelper(self, node: Node, word: str):
        curr = node
        for letter in word:
            if letter in curr.children.keys():
                curr = curr.children[letter]
            else:
                curr.children[letter] = self.Node(letter)
                curr = curr.children[letter]
        if curr.end == True:
            return False
        curr.end = True
        return True
    
    def contains(self, word: str) -> bool:
        if word == "":
            return True
        return self.containsHelper(self.root, word)

    def containsHelper(self, node: Node, word: str) -> bool:
        curr = node
        for letter in word:
            if letter in curr.children.keys():
                print(curr.value, end=", ")
                curr = curr.children[letter]
            else:
                return False
        print(curr.value)
        return curr.end

    def containsPrefix(self, prefix: str) -> bool:
        return self.containsPrefixHelper(self.root, prefix)

    def containsPrefixHelper(self, node: Node, prefix: str) -> bool:
        curr = node
        for letter in prefix:
            if letter in curr.children.keys():
                curr = curr.children[letter]
            else:
                return False
        return True

if __name__ == "__main__":
    x = Trie()
    print(x.root.children)
    x.add("yes")
    x.add("cisco")
    print(x.root.children)
    print(x.contains("yes"))
    print(x.containsPrefix("ye"))
    print(x.contains("cis"))
    print(x.add(""))
    print(x.contains(""))