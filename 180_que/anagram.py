def findAnagram(s, p):
    prime= {'a':2,
        'b': 3, 
        'c' : 5, 
        'd' : 7, 
        'e' : 11, 
        'f' : 13, 
        'g' : 17, 
        'h' : 19, 
        'i' : 23, 
        'j' : 29, 
        'k' : 31, 
        'l' : 37, 
        'm' : 41, 
        'n' : 43, 
        'o' : 47, 
        'p' : 53, 
        'q' : 59, 
        'r' : 61, 
        's' : 67, 
        't' : 71, 
        'u' : 73, 
        'v' : 79, 
        'w' : 83, 
        'x' : 89, 
        'y' : 97, 
        'z': 101}
    res=[]
    j = len(p)
    phash =0
    for l in p:
        phash += prime[l]*(ord(l)-ord("a")+1)
    for i in range(len(s)-j+1):
        print s[i:j]
        shash =0
        for k in s[i:j]:
            shash += prime[k]*(ord(l)-ord("a")+1)
        if phash == shash:
            res.append(i)
        j+=1
        print shash, phash
    return res


s= "cbaaebbacd"
p= "abc"
# s= "af"
# p="be"
# s = "op"
# p ="by"
print findAnagram(s, p)
# [0,6]