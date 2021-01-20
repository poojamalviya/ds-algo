def merge(intervals):
    intervals.sort(key= lambda x:x[0])
    res =[]
    to_push =intervals[0]
    for a in range(1, len(intervals)):
        if to_push[1]>=intervals[a][0]:
            to_push[0], to_push[1]=min(to_push[0], intervals[a][0]), max(to_push[1], intervals[a][1])

        else:
            res.append(to_push)
            to_push = intervals[a]
    res.append(to_push)
        
    return res
            


a = [[1,3],[2,6],[8,10],[15,18]]

# o/p [[1,6],[8,10],[15,18]]
print merge(a)