def pascal(row):
    tri=[]
    for i in range(row):
        r = [None for _ in range(i+1)]
        r[0], r[-1] =1, 1

        for j in range(1, len(r)-1):
            r[j] = tri[i-1][j-1] + tri[i-1][j]
        tri.append(r)

    return tri


print pascal(4)