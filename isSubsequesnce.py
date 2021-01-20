def isSubSequence(str1, str2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if str1[m-1] == str2[n-1]:
        return isSubSequence(str1, str2, m-1 , n-1)
    else:
        return isSubSequence(str1, str2, m , n-1)


string1 = "gksrek"
string2 = "geeksforgeeks"
m = len(string1) 
n = len(string2) 
if isSubSequence(string1, string2, m, n): 
    print "Yes"
else: 
    print "No"
