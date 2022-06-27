from random import randint

def quick_sort(a: int):
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


    
if __name__ == '__main__':
    size = input("Enter the size of the list to sort: ")
    myList = [randint(1,int(size)) for x in range(int(size))]
    print(myList)
    quick_sort(myList)
    print(myList)
    for index, value in enumerate(myList):
        if  index > 0 and value < myList[index - 1]:
            print("ERROR")
            print(f"{index}:{value} < {index - 1}:{myList[index - 1]}")