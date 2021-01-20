
def lengthOfLongestSubstring(s):
    i = 0
    j = 0
    res =0
    mset = set()
    while j < len(s) and i< len(s):
        print i, j, "i, j"
        print mset
        if not (s[j] in mset):
            print s[j], "add"
            mset.add(s[j])
            j = j+ 1
            res = max(res, len(mset))
            print res, "res"
        else:
            print s[i], "remove"
            mset.remove(str(s[i]))
            i += 1
    return res




a ="abcabcbb"
print lengthOfLongestSubstring(a)

