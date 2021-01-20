def climb(step, s, n):
    if s == 0:
        return 1
    if s <0:
        return 0
    if n == 0 and s != 0:
        return 0
    return (climb(step, s-step[n-1], n)+ climb(step, s, n-1))


step = [1,2]
s = 4
print(climb(step, s, 2))