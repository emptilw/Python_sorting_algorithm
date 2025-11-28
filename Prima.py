import sys

V = 8
graph = [
    [0,2,5,1,0,0,1,0],
    [2,0,0,3,1,0,0,0],
    [5,0,0,0,2,4,4,0],
    [1,3,0,0,9,0,9,4],
    [0,1,2,9,0,3,0,0],
    [0,0,4,0,3,0,0,1],
    [1,0,4,9,0,0,0,6],
    [0,0,0,4,0,1,6,0]
]

def primMST(graph):
    key = [sys.maxsize]*V
    parent = [None]*V
    mstSet = [False]*V

    key[0] = 0
    parent[0] = -1

    for _ in range(V):
        u = min((k if not mstSet[i] else sys.maxsize, i) for i, k in enumerate(key))[1]
        mstSet[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]+1} - {i+1} \t{graph[i][parent[i]]}")

primMST(graph)
