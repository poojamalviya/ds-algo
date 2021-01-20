def editDistance(str1, str2, m, n):
    if m == 0:
        return m
    if n == 0:
        return n
    if str1[m-1] == str2[n-1] :
        return editDistance(str1, str2, m-1, n-1)
    
    return 1+ min(editDistance(str1, str2, m, n-1), #add 
                    editDistance(str1, str2, m-1, n), #delete
                    editDistance(str1, str2, m-1, n-1))  #replace



str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)))