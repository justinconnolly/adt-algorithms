class BinaryHeap():
    def __init__(self):
        self.a = []

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i -  1) // 2

    def add(self, x):
        self.a.append(x)
        self.bubble_up(len(self.a) - 1)

    def bubble_up(self, i):
        p = self.parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            prev = self.a[i]
            self.a[i] = self.a[p]
            self.a[p] = prev
            i = p
            p = self.parent(i)

    def remove(self):
        x = self.a[0]
        self.a[0] = self.a.pop()
        self.trickle_down(0)
        return x
    
    def trickle_down(self, i):
        while i >= 0:
            j = -1
            r = self.right(i)
            if r < len(self.a) and self.a[r] < self.a[i]:
                l = self.left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = self.left(i)
                if l < len(self.a) and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                k = self.a[j]
                self.a[j] = self.a[i]
                self.a[i] = k
            i = j
x = BinaryHeap()
print(x.parent(6))
x.add(5)
x.add(3)
x.add(4)
x.add(2)
x.remove()
print(x.a)
