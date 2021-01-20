import time
def stockwithcoolingperiod(arr):
    rest, buy, sell=[0]*len(arr),[0]*len(arr),[0]*len(arr)
    rest[0]=0
    buy[0]= -arr[0]
    sell[0]=  float('-inf')
    for i in range(1, len(arr)):
        rest[i] = max(rest[i-1], sell[i-1])
        buy[i] = max(buy[i-1], rest[i-1]-arr[i])
        sell[i] = max(sell[i-1], buy[i-1]+arr[i])

    return max(rest[-1], sell[-1])
    

arr =[1,2,3,0,2]
print stockwithcoolingperiod(arr)
# print maxProfit(arr)