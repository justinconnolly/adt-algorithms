import singlyLinkedList

class HashTable:
    class Node:
        next = None
        prev = None
        value = None
        def __init__(self,x):
            self.value = x
  
    def __init__(self):
        self.backingArray = [self.Node(None) for x in range(5)]
        self.size = 0

    def add(self, x):
        bucket = hash(x) % len(self.backingArray)
        if self.backingArray[bucket].value == None:
            self.backingArray[bucket].value = x
        else:
            i = 0
            curr = self.backingArray[bucket]
            while curr != None:
                prev = curr
                curr = curr.next
            if prev.value == x:
                return False
            prev.next = self.Node(x)
        return True

    def remove(self, x):
        bucket = hash(x) % len(self.backingArray)
        curr = self.backingArray[bucket]
        prev = None
        while curr != None:
            if curr.value == x:
                if prev is not None:
                    prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev
                if curr.next is None and curr.prev is None:
                    self.backingArray[bucket] = self.Node(None)

                return True
            prev = curr
            curr = curr.next
        return False

    def contains(self, x):
        pass

    def __repr__(self):
        for x in self.backingArray:
            while x is not None:
                print(str(x.value), end = "")
                if x.next is not None:
                    print(", ", end= "")
                x = x.next
            print()
        return ""




ht = HashTable()
# print(ht.add(1))
# print(ht.add(1))
# print(ht.remove(1))
# print(ht.remove(1))
print(ht.remove(1))
print(ht)

for x in range(17):
    ht.add(x)
# ht.add("x")
# ht.remove("x") 
for x in range(5):
    ht.remove(x*5)
print(ht)
