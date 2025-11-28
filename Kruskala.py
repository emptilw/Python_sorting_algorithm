class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)

edges = [
    Edge(0,1,2), Edge(0,2,5), Edge(0,3,1), Edge(0,6,1),
    Edge(1,3,3), Edge(1,4,1), Edge(2,4,2), Edge(2,5,4),
    Edge(2,6,4), Edge(3,4,9), Edge(3,6,9), Edge(3,7,4),
    Edge(4,5,3), Edge(5,7,1), Edge(6,7,6)
]

edges.sort(key=lambda e: e.w)
parent = [i for i in range(V)]

print("Edge \tWeight")
for e in edges:
    x = find(parent, e.u)
    y = find(parent, e.v)
    if x != y:
        print(f"{e.u+1} - {e.v+1} \t{e.w}")
        union(parent, x, y)
