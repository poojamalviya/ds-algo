import collections
def detectCycle(numCourses, prerequisites):
    visited = [0]* numCourses
    graph = collections.defaultdict(set)
    for i in prerequisites:
        x, y = i[0], i[1]
        graph[x].add(y)
    def dfs(i):
        if visited[i] == 1:
            return True
        if visited[i] ==-1:
            return False
        visited[i] =-1
        for node in graph[i]:
            if not dfs(node):
                return False
        visited[i] =1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


numCourses = 4
prerequisites = [[1,0], [0,1]]
    # while len(white)>0:
print detectCycle(numCourses, prerequisites)