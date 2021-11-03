"""
Need a balance() method for the a linked list gets too large/small (ie maybe 2n or n/3).
"""

import singlyLinkedList

class HashSet:
    backingArray = []
    def __init__(self):
        self.backingArray = [singlyLinkedList.linkedList() for x in range(10)]

    def __repr__(self):
        for x in self.backingArray:
            print(x)
        return "Done"
        

    def add(self, value):
        bucket = hash(value) % len(self.backingArray)
        self.backingArray[bucket].push(value)

    def remove(self, value):
        bucket = hash(value) % len(self.backingArray)
        indexOfValue = self.contains(value)
        print(indexOfValue)
        if indexOfValue >= 0:
            self.backingArray[bucket].remove(indexOfValue)
            return True
        return False
        
    
    def contains(self, value) -> int:
        bucket = hash(value) % len(self.backingArray)
        sll = self.backingArray[bucket].getHead()
        counter = 0
        while sll != None:
            if sll.value == value:
                return counter
            sll = sll.next
            counter += 1
        return -1


if __name__ == "__main__":
    from random import randint
    x = HashSet()
    for i in range(20):
        x.add(round(randint(1,50) * 1.22,1))
    print(x)
