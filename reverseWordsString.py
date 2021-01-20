
def reverseWordsString(s):
    res = ""
    arr= s.split()
    for i in range(len(arr)-1, -1, -1):
        res = res + arr[i]
    return res


s = "the sky is blue"
# s= "  hello world!  "
# s = "a good   example"

print (reverseWordsString(s))