def longestPalindromicSubse(mstr, l, h):
    if l == h:
        return 1
    if mstr[l] == mstr[h] and l+1 == h:
        return 2
    if mstr[l] == mstr[h]:
        return longestPalindromicSubse(mstr, l+1, h-1)
    return max(longestPalindromicSubse(mstr, l+1, h), (mstr, l, h-1))
    


mstr = 'babad'
n = len(mstr)
ll =longestPalindromicSubse(mstr, 0, n-1)
print(ll)

