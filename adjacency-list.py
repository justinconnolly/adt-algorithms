from random import randint, sample

def make_list(size: int):
    aList = []
    for i in range(size):
        nodeList = list(range(size))
        nodeList.remove(i)
        numEdges = randint(1,4)
        outEdges = sample(nodeList, numEdges)
        aList.append(outEdges)
    return aList

#BFS to get distance between nodes
def distance(start: int, target: int, graph: list):
    seen = [False] * len(graph)
    queue = []
    queue.append(start)
    seen[start] = True
    level = 1
    while len(queue) > 0:
        i = queue.pop(0)
        for j in graph[i]:
            if not seen[j]:
                seen[j] = True
                queue.append(j)
            if j == target:
                return level
        level += 1
        

    return "No connecting path"




if __name__ == '__main__':
    adj_list = make_list(5)
    print(adj_list)
    print(distance(0,1,adj_list))
