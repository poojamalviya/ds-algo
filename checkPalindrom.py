def isPal(string, s, e):
    print s, e
    if s == e:
        return True
    if s >e :
        return False
    if string[s] == string[e]:
        return isPal(string, s+1, e-1)


str1 = [1,2,3,2,1]
end = len(str1)
print(isPal(str1, 0, end -1))
