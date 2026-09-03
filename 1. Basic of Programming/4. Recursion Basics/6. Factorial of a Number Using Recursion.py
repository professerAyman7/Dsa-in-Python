# Why 2 base case when the function cannot go to 0 - because if user enter 0 then it will throw an error but factorial of 0 is 1 thats why we have 2 base case

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number to print factorial: "))
print(factorial(n))


'''
Time  Complexity - O(n)
Space Complexity - O(n) - stack space
'''