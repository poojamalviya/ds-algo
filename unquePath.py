
def findPath(r, c):

    if r == 1 or c == 1:
        return 1

    return findPath(r-1, c) + findPath(r, c-1) 



sol =0

print(findPath(3, 3))