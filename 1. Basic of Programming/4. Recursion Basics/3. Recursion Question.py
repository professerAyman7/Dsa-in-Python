# 1 to N using tail recursion

def tailRecursion(i):
    if i == 0:
        return
    tailRecursion(i-1)
    print(i)

tailRecursion(4)