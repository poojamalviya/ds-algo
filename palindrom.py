def checkPalindrom(s):
    mid = len(s)-1 /2
    for i in range(0, mid):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


str1= "madam"
print (checkPalindrom(list(str1)))