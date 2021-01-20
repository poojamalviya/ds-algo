def setZeroes(m):
    r = len(m)
    c = len(m[0])
    is_col =False
    
    for i in range(r):
        if m[i][0] == 0:
            is_col = True
        for j in range(1,c):
            if m[i][j] ==0:
                m[i][0] =0
                m[0][j] =0
    for i in range(1,r):
        for j in range(1,c):
            if m[i][0] == 0 and m[0][j] ==0:
                m[i][j]=0
    if m[0][0]==0:
        for j in range(c):
            m[0][j]=0
    if is_col:
        for i in range(r):
            m[i][0] = 0
    print m


a=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

setZeroes(a)


