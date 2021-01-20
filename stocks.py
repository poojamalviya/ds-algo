
import sys

def maxProfit(arr):
    mini = sys.maxsize
    diff = 0
    for i in arr:
        if i >= mini:
            diff = max(diff, i - mini)
        else:
            mini = i
    return diff


arr = [7,1,5,3,6,4]
n = len(arr)
print (maxProfit(arr))
