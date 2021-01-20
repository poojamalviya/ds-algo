def KMPSearch(txt, pat):
    prefixTable = len(pat)*[0]
    length, i =0, 1 # i =1
    while i<len(pat):
        if pat[i] == pat[length]:
            length +=1
            prefixTable[i]= length
            i +=1
        else:
            if length !=0:
                length=prefixTable[length-1]
            else:
                prefixTable[i] =0
                i +=1
    i =0
    j =0
    while i<len(txt):
        if txt[i]==pat[j]:
            i +=1
            j +=1
        if j== len(pat):
            return i-j
        elif i< len(txt) and txt[i] != pat[j]:
            if j !=0:
                j = prefixTable[j-1]
            else:
                i= i+1
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB" 
# [A    B   A   B   C   A   B   A   B]
# [0    0   1   2   0   1   2   3   4]
print KMPSearch(txt, pat)

