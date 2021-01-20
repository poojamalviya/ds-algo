def meetingRoom(a):
    a.sort(key = lambda x :x[0])
    for i in range(len(a)-1):
        if a[i][1]> a[i+1][0]:
            return False
    return True



a = [[0,30], [5,10], [15,20]] #[[7, 20], [2,4]]
print meetingRoom(a)


def meetingRoomTwo(a):
    if a == None or len(a) == 0:
        return 0
    res= 1
    for i in range(len(a)-1):
        if i[i][1]> 



a =[[0,30], [5,10], [15, 20]]