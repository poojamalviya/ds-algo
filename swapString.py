def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    one, two, temp =None, None, None
    for i in range(len(A)):
        if A[i] != B[i]:
            if one is None:
                one = i
            else:
                two =i
    if one is not None and two is not None:            
        temp = A[0:two-1] + A[two] +A[two+1:one-1] +A[one] + A[one+1:len(A)-1] 

    if temp is not None:
        print temp
        for i in range(0, len(temp)-1):
            if temp[i] != B[i]:
                return False
    else:
        for i in range(0, len(A)):
            if A[i] != B[i]:
                return False
    return True


A = "aaaaaaabc" #aa #abab
B = "aaaaaaacb" #aa  #abab
print(buddyStrings(A, B))
# aaaaaaacbc