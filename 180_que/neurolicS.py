def subString(s, n):
    res = []
    for i in range(n): 
        for len in range(i+1,n+1):
            res.append(s[i:len])
    res.sort()
    return res
  
# s = "banana"
s ="ba"

# print subString(s,len(s))

# print findSubsets(['b','a','n','a','n','a'], 0)

import requests
def getUserName(num):
    res =[]
    response = []
    count = 10
    a = requests.get("https://jsonmock.hackerrank.com/api/article_users?page=1")
    b = requests.get("https://jsonmock.hackerrank.com/api/article_users?page=2")
    a = a.json()
    b = b.json()
    res = a['data'] + b['data']
    print len(res)
    for i in range(len(res)):
        if res[i]['submission_count']> 10:
            response.append(res[i]['username'])
    print response
    


getUserName(10)