def product(x, y, prod):
    if y ==0:
        return prod
    return product(x, y-1, prod+x)

x= 9
y= 8

print(product(x, y, prod=0))