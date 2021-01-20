def climbStairs(stairs):
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0
    res = climbStairs(stairs-1) + climbStairs(stairs-2)

    return res

step = [1,2]
stairs = 5

print climbStairs(stairs)