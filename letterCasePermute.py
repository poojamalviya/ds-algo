
def permute(s):
    res =[]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            
    return res

def recur(s):
    res= []
    dfs(s, 0, "", res)
    return res

def dfs(s, index, temp, res):
    if len(s)== len(temp):
        res.append(temp)
    else:
        if s[index].isalpha():
            dfs(s, index+1, temp+s[index].swapcase(), res)
        dfs(s,index+1, temp+s[index], res)

s= "a1b2"

print permute(s)
print recur(s)