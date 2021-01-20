def allpossiblebinar(s, n, i):
    if i == n:
        # print(''.join(s)) 
        print s
        return 
    if s[i] == '?' :
        s[i] = 0
        allpossiblebinar(s, n , i+1)
        s[i] =1 
        allpossiblebinar(s, n , i+1)
        s[i] = '?'
    else:
        allpossiblebinar(s, n , i+1)
    

str1= "1??0?101"
str1 = list(str1)
allpossiblebinar(str1, len(str1)-1, 0)

