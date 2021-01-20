def powerof4(num):
    while num>0:
        print num, "num"
        num = num%4
        if num ==0:
            return True
        # num = num/4
    return False

print powerof4(16)
print powerof4(64)
print powerof4(19)