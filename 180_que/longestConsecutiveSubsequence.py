def longest_consecutive_subsequence(a):
    if len(a)==0:
        return 0
    longest = 0
    s = set(a)
    for i in range(0, len(a)):
        if a[i] -1 not in s:
            cur = a[i]
            cur_s = 1
            while cur+1 in s:
                cur = cur+1
                cur_s = cur_s+1

            longest = max(cur, cur_s)
    return longest
    
                


a = [100, 4, 200, 1, 3, 2]
print longest_consecutive_subsequence(a)