def reArrange(arr):
    even, odd = 0, 1
    while even < len(arr) and odd < len(arr):
        if arr[even]%2 :
            arr[even], arr[odd] = arr[odd], arr[even]
            odd +=2
        else:
            even += 2
    return arr


        

        

arr = [648,831,560,986,192,424,997,829,897,843] #[4,2,5,7]
    # [ 0,  1,  2 , 3,  4,  5,  6,  7,  8,  9]
print(reArrange(arr))