from random import randint

def it_quick_sort(a: int):
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


    
if __name__ == '__main__':
    size = input("Enter the size of the list to sort: ")
    myList = [randint(1,int(size)) for x in range(int(size))]
    print(myList)
    re_quick_sort(myList)
    print(myList)
    for index, value in enumerate(myList):
        if  index > 0 and value < myList[index - 1]:
            print("ERROR")
            print(f"{index}:{value} < {index - 1}:{myList[index - 1]}")