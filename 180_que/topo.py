import collections
# WHITE = 1
# GREY = 2
# BLACK =3
# def courseSchedule2(n, arr):
#     size = len(arr)
#     adj_list = defaultdict(list)
#     for dest, src in arr:
#         adj_list[src].append(dest)

#     topological_sorted_order =[]
#     is_possible = True

#     color = {k: WHITE for k in range(n)}

#     def dfs(vertex):
#         nonlocal is_possible
#         if not is_possible:
#             return 
#         color[vertex] = GREY
#         if vertex in adj_list:
#             for neighbor in adj_list[vertex]:
#                 if color[neighbor] ==WHITE:
#                     dfs(neighbor)
#                 elif color[neighbor]==GREY:
#                     is_possible = False
#         color[vertex] = BLACK
#         topological_sorted_order.append(vertex)
    
#     for vertex in range(n):
#         if color[vertex] == WHITE:
#             dfs(vertex)
#     return topological_sorted_order

        
import collections
def topoDfs(n, arr):
    dic = collections.defaultdict(set)
    neigbor = collections.defaultdict(set)
    for i , j in arr:
        dic[i].add(j)
        neigbor[j].add(i)

    stack = [i for i in range(n) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigbor[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res

def findOrder(numCourses, prerequisites):
    import collections
    dic = collections.defaultdict(set)
    neig = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neig[j].add(i)
    print dic
    print neig
     
    stack  = [i for i in range(numCourses) if not dic[i]]
    res= []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neig[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res
arr= [[1,0],[2,0],[3,1],[3,2]]
n = 4
# print findOrder(n,arr)

# 'A' -> ['C', 'D', 'F']
# 'C' -> ['B', 'E']
# ['B', 'E', 'C', 'D', 'F', 'A']

# edge (A, C), (A, D),(A, F), (C, B), (C, E)

from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,v) 
    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        print stack 
  
g= Graph(5) 
g.addEdge(1, 0); 
g.addEdge(0, 1); 
g.topologicalSort() 

def topoutil(v, adjlist, visited, res):
    visited.append(v)
    for i in adjlist[v]:
        if i not in visited:
            topoutil(i, adjlist, visited, res)
    res.append(v)
    
def topo(edges):
    adjlist = collections.defaultdict(set)
    for i, j in edges:
        adjlist[i].add(j)
    
    print adjlist, "adjlist"
    visited =[]
    res =[]
    for vertex in adjlist.keys():
        if vertex not in visited:
            topoutil(vertex,adjlist, visited, res)
    return res
print topo([('A', 'C'), ('A', 'D'),('A', 'F'), ('C', 'B'), ('C', 'E')])
# print topo([(0, 1), (1, 0)])
