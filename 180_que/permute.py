def permute(s, temp, res, level):
    if len(temp) == len(s):
        res.append(temp)
    if level == 3:
        return res
    permute(s, temp.append(s[level]), res, level+1)
    permute(s, temp.pop(), res , level+1)


def subsets_of_size (array, size, start=0, prepend=None):
    if prepend is None:
        prepend = [] # Standard Python precaution with modifiable defaults.
    if 0 == size:
        return [[] + prepend] # Array with one thing.  The + forces a copy.
    elif len(array) < start + size:
        return [] # Array with no things.
    else:
        answer = subsets_of_size(array, size, start=start + 1, prepend=prepend)
        prepend.append(array[start])
        answer = answer + subsets_of_size(array, size-1, start=start + 1, prepend=prepend)
        prepend.pop()
        return answer

# print subsets_of_size([1,2,3,4,5], 2)


    
    

# s = ['a', 'b', 'c']
# res =[]
# temp =[]
# print (permute(s, temp, res, 0))
def letTry(s, l, r):
    res =[]
    if l == r:

        print s
    for i in range(l, r):
        s[i], s[l] = s[l], s[i]
        letTry(s, l+1, r)
        s[i], s[l] = s[l], s[i]

letTry(['a','b','c'], 0, len(['a','b','c']))