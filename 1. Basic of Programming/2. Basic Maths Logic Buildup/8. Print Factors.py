# Optimul Solution

from math import sqrt
def factors(num):
    factor = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            factor.append(i)
            if num // i != i:
                factor.append(num//i)
    # If we want to print in sorted manner then sort it!!
    return factor

num = int(input("Enter a number: "))
print(f"The factor of the numbers is: {factors(num)}")

'''
Time  Complexity - O(sqrt(n)) and if we sort it then O(sqrt(n)) + O(nlog n)
Space Complexity - O(1) - if we ignore the return [list]
'''