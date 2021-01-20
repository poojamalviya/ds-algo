class Solution:
    def wordBreak(self, s, wordDict):
        dp = {}
        def word_break(s):
            print s

            if s in dp: return dp[s]
            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s): result.append(w)
                    else:
                        tmp = word_break(s[len(w):])
                        # print tmp, "= = "
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            print dp
            return result      
        return word_break(s)

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
a =Solution()
aa = a.wordBreak(s, wordDict)
print aa
import time 
def wordBreak2(s, di):
    dp ={}
    return util(s, di, dp)
def util(s, di, dp):
    res = []
    if s in dp: return dp[s]
    for w in di:
        if s[:len(w)]== w:
            if len(w) == len(s):
                res.append(w)
            else:
                tmp = util(s[len(w):], di, dp)
                for t in tmp:
                    res.append(w + " " + t)
    dp[s] = res
    return res

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print wordBreak2(s, wordDict)
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]