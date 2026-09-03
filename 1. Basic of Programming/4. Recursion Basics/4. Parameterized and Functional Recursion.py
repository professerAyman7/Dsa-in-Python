# Why doesnt it print in return sum

def newFunction(sum, i, n):
    if i > n:
        print(sum)
        return
    newFunction(sum+i, i+1, n)

newFunction(0, 0, 10)