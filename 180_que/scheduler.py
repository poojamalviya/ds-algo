import collections

def scheduler(task, n):
    counter = collections.Counter(task)
    pp= counter.most_common(1)
    print pp




tasks = ["A","A","A","B","B","B"] 
n = 2
# [a, b , #, a, b , #, a, b]
print scheduler(tasks, n)

3*2
res = 