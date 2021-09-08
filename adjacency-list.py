from random import randint, sample

def make_list(size: int):
    aList = []
    for i in range(size):
        nodeList = list(range(size))
        nodeList.remove(i)
        numEdges = randint(0,4)
        outEdges = sample(nodeList, numEdges)
        aList.append(outEdges)
    return aList



if __name__ == 'main':
    adj_list = make_list(5)
    print(adh_list)