# - Input: List of tuples (timestamp, #drivers) for 2 cities
# - Output: List of tuples with combined number of drivers in both cities for existing timestamps.
# /* 
# Bangalore
# (1:00, 10), (1:05, 12), (1:15, 20), (2:00, 9)
# */

# /* 
# Kolkata
# (1:03, 11), (1:05 11), (1:30, 3), (2:30, 4)
# */

# /*
# total
# (1:00, 10), (1:03, 21), (1:05, 23), (1:15, 31), (1:30, 23), (2:00, 12), (2:30, 13)
# */

class Drivers():
    def __init__(self, city, time):
        cityMap = {}
        cityMap[city] = set(time) # bangalore : set[(1:00, 10), (1:05, 12), (1:15, 20), (2:00, 9)]
        isLast = time[0]
    

bangalore  = Drivers("bangalore", [("1:00", "10"), ("1:05", "12"), ("1:15", "20"), ("2:00", "9")])
kolkata = Drivers("kolkata", [("1:03", "11"), ("1:05", "11"), ("1:30", "3"), ("2:30", "4")])

def getTotal(bangalore, kolkata):
    print bangalore.isLast
    res =[]
    l1, l2= len(bangalore.cityMap), len(kolkata.cityMap)
    print l1, l2
    if l1>0 and l2>0:
        for i in range(l1): 
            for j in range(l2):
                time1, number1 = bangalore.cityMap[i]
                time2, number2 = kolkata.cityMap[j]
                if time1==time2:
                    res.append((time1, number1+number2))
                    bangalore.isLast = (time1, number1)
                    kolkata.isLast = (time2, number2)
                elif time1 >time2:
                    res.append(time2,  number2+ bangalore.isLast[1])
                else:
                    res.append(time1,  number1+ kolkata.isLast[1])
    elif l1:
        res +=l1
    elif l2:
        res +=12
    return res
                

getTotal(bangalore, kolkata)



