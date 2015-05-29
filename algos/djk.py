def djk(graph, vertices, source):
    Q = []
    dist = {}
    prev = {}

    dist[source] = 0
    prev[source] = None

    for vertex in vertices:
        if vertex != source:
            dist[vertex] = float("inf")
            prev[vertex] = None
        Q.append(vertex)

    while len(Q) > 0:
        distCopy = dist.copy()

        for vertex in vertices:
            if vertex not in Q:
                del distCopy[vertex]

        #print distCopy
        u = min(distCopy, key=distCopy.get)
        #print u
        Q.remove(u)

        neighbors = graph[u]
        for neighbor in neighbors.keys():
            alt = dist[u] + neighbors[neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u

    return dist, prev

if __name__ == "__main__":
    graph = {'s':{'u':10, 'x':5},
             'u':{'v':1, 'x':2},
             'v':{'y':4},
             'x':{'u':3, 'v':9, 'y':2},
             'y':{'s':7, 'v':6}}
    vertices = ['s','u','v','x','y']

    dist, prev = djk(graph,vertices,'s')

    print dist
    print prev