def findTriplets(arr):
    temp =[]
    max1=0
    max2 =0
    for i in range(len(arr)-2):
        for j in range(i, len(arr)):
            if j< len(arr) and j+1 < len(arr) and j+2 <len(arr):
                aa = [arr[j], arr[j+1], arr[j+2]]
                aa.sort()
                if max1 < aa[1]:
                    max2 = max1
                    max1 = aa[1]
                if max1 == aa[1]:
                    max2 = aa[1]
                temp.append(aa)
    return max1 + max2



# def findMaxTriplet(arr):
#     temp = []
#     c =0
#     aa =[]
#     for i in range(len(arr)):
#         c= c+1
#         aa.append(arr[i])
#         if c ==3:
#             aa.sort()
#             temp.append(aa)
#             c=0
#             aa= []

#         # if c == 3:
#         #     aa.sort()
#         #     temp.append(aa)
#         #     c=0
#         #     aa =[]
#         # else:
#         #     aa.append(arr[i])
#         #     c= c+1
#     print temp





arr = [5, 2, 8, 5, 1, 5]

# findMaxTriplet(arr)

print findTriplets(arr)