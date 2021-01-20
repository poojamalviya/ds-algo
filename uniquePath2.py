
def findPath(m, r , c):
    if m[r][c]== 1:
        return 0
    if r==2 or c ==2:
        return 1
    return findPath(m, r+1, c) + findPath(m, r, c+1)





m = [ [0,0,0],
      [0,1,0],
      [0,0,0] ]

r= 0
c= 0
print findPath(m, r, c)