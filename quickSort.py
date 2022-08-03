from random import randint

# recursive random quicksort
def random_re_quick_sort(a: int):
    quickSort(a,0,len(a))

def quickSort(myList: list, start: int, end: int):
    if end <= 1:
        return

    pivot = myList[start + randint(0,end - 1)]
    p = start - 1
    j = start
    q = start + end

    while j < q:
        if myList[j] < pivot:
            p += 1
            myList[j], myList[p] = myList[p], myList[j]
            j += 1
        elif myList[j] > pivot:
            q -= 1
            myList[j], myList[q] = myList[q], myList[j]
        else:
            j += 1
            
    quickSort(myList, start, p - start + 1)
    quickSort(myList, q, end - (q - start))

# basic recursive quicksort
def re_quick_sort(A):
    re_quickSort(A, 0, len(A) - 1)

def re_quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        re_quickSort(A, p, q - 1)
        re_quickSort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# randomized recursive quicksort
def randomized_QS(A):
    from random import randint
    randomized_quick_sort(A,0,len(A) - 1)

def randomized_partition(A, p, r):
    i = randint(p,r)
    A[r], A[i] = A[i], A[r]
    return randomized_partition(A, p, r)

def randomized_quick_sort(A, p, r):
    if p < r:
        q =  randomized_partition(A, p, r)
        randomized_quick_sort(A, p, q - 1)
        randomized_quick_sort(A, q + 1, r)


def hoare_quicksort(A, left, right):
    if left < right:
        p = hoare_partition(A, left, right)
        hoare_quicksort(A, left, p)
        hoare_quicksort(A, p + 1, right)

def hoare_partition(A, left, right):
    pivot = A[randint(left, right)]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while A[i] < pivot:
            i += 1
        j -= 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]
        
    
if __name__ == '__main__':
    # size = input("Enter the size of the list to sort: ")
    size = 15
    myList = [randint(1,int(size)) for x in range(int(size))]
    print(myList)
    # randomized_QS(myList)
    hoare_quicksort(myList, 0, len(myList) - 1)
    print(myList)
    for index, value in enumerate(myList):
        if  index > 0 and value < myList[index - 1]:
            print("ERROR")
            print(f"{index}:{value} < {index - 1}:{myList[index - 1]}")