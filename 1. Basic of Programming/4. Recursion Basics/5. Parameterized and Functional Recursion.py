def newFunction(n):
    if n == 1:
        return 1
    return n + newFunction(n-1)

n = int(input("Enter a number: "))
print(newFunction(n))


'''
Time  Complexity - O(n)
Space Complexity - O(n) - stack space
'''