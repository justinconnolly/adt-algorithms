from random import randint

def mergeSort(fullList: list):
    if len(fullList) <= 1:
        return
    firstHalf = list(fullList[0:len(fullList)//2])
    secondHalf = list(fullList[len(fullList)//2:len(fullList)])
    mergeSort(firstHalf)
    mergeSort(secondHalf)
    merge(firstHalf, secondHalf, fullList)

def merge(firstHalf: list, secondHalf: list, fullList: list):
    firstCounter = 0
    secondCounter = 0
    for index, value in enumerate(fullList):
        if firstCounter == len(firstHalf):
            fullList[index] = secondHalf[secondCounter]
            secondCounter += 1
        elif secondCounter == len(secondHalf):
            fullList[index] = firstHalf[firstCounter]
            firstCounter += 1
        elif firstHalf[firstCounter] <= secondHalf[secondCounter]:
            fullList[index] = firstHalf[firstCounter]
            firstCounter += 1
        else:
            fullList[index] = secondHalf[secondCounter]
            secondCounter += 1


if __name__ == '__main__':
    size = input("Enter the size of the list to sort: ")
    myList = [randint(1,int(size)) for x in range(int(size))]
    print(myList)
    mergeSort(myList)
    print(myList)