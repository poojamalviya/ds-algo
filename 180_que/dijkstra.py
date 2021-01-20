def selectMinVertex(value, processed):
    imin= float('inf')
    for i in range(len(value)):
        if value[i]<imin and not processed[i]:
            minVertex = i
    return minVertex
def dijkstra(graph):
    n = len(graph)
    parent = [-1]*n
    processed = [False]*n
    value = [float('inf')]*n
    value[0] =0
    for _ in range(n-1):
        U = selectMinVertex(value, processed)
        processed[U] = True
        for j in range(n):
            if(graph[U][j]!=0 and processed[j]==False and value[U]!=float('inf') and (value[U]+graph[U][j] < value[j])):
                value[j] = value[U]+graph[U][j]
                parent[j] = U

    for i in range(1, n):print "U-V: ", parent[i], "->", i, " wt= ", graph[parent[i]][i],
graph=                 [ [0, 1, 4, 0, 0, 0],
						[1, 0, 4, 2, 7, 0],
						[4, 4, 0, 3, 5, 0],
						[0, 2, 3, 0, 4, 6],
						[0, 7, 5, 4, 0, 7],
						[0, 0, 0, 6, 7, 0]]
dijkstra(graph)
# TIME COMPLEXITY: O(V^2)
# TIME COMPLEXITY: (using Min-Heap + Adjacency_List): O(ElogV)