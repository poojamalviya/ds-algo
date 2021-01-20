def removeDuplicate(arr):
    for i in range(0, len(arr)-2):
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
    return arr


arr=[1,1,3,4,5,6,6]
print(removeDuplicate(arr))



def mysterious_recursive_function(number):
    """
    Mysterious recursive function
    :param number:
    :return: mysterious number
    """
    return number * mysterious_recursive_function(number - 1)

# check output for input 5
print(mysterious_recursive_function(5))