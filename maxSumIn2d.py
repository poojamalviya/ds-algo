def minSum(m, r, c, mins):
    print r , c
    if r == 2 and c == 2 :
        return mins+ m[r][c]
    print mins
    mins = mins + min(minSum(m, r+1, c, mins), minSum(m, r, c+1, mins))
    return mins



m =[ [1,3,1],
     [1,5,1],
     [4,2,1] ]  

p = minSum(m, 0, 0, 0)
print p
