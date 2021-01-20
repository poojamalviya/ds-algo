def wordBreak(s, d):
    if len(s)==0:
        return True
    
    for word in d:
        size = len(word)
        if s[0:size] in d and wordBreak(s[size:], d):
            return True
    return False

def dpWordBreak(s, d):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for w in d:
            # print dp[i-len(w)], i-len(w), i
            if dp[i-len(w)] and s[i-len(w):i]==w:
                dp[i]= True
    print dp
    return dp[-1]




# s = 'catsandog'
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "leetcode"
# wordDict = ["leet", "code"]
# s = "applepenapple" 
# wordDict = ["apple", "pen"]
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"]

s = "bb"
wordDict = ["a","b","bbb","bbbb"]
print wordBreak(s, wordDict)
print dpWordBreak(s, wordDict)