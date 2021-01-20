def knapsack(val,wt, s, i):
    if i is 0 or s is 0:
        return 0
    if wt[i]> s:
        knapsack(val, wt, s, i-1)
    else:
        t1=  knapsack(val, wt, s, i-1)
        t2 = val[i-1] + knapsack(val, wt, s-wt[i], i-1)
        return (max(t1, t2))

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
index = len(wt)-1
print(knapsack(val,wt, W, index))