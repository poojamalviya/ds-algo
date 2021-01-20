def paintHouse(costs):
    ans = 1000
    for i in range(len(costs[0])):
        res =0
        res =costs[0][i]
        for j in range(len(costs[1])):
            if j==i:
                continue
            res +=costs[1][j]
            for k in range(len(costs[2])):
                if j==k:
                    continue
                res += costs[2][k]
                print res
                ans = min(res, ans)
    return ans
        


arr= [[14,2,11],[11,14,5],[14,3,10]]
print paintHouse(arr)


     