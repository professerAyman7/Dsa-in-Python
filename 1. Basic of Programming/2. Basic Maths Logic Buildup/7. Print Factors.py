# Better Solution

def factors(num):
    factor = []
    for i in range(1, (num//2)+1):
        if num % i == 0:
            factor.append(i)
    factor.append(num)
    return factor

num = int(input("Enter a number: "))
print(f"The factor of the numbers is: {factors(num)}")

'''
Time  Complexity - O(n/2) - O(n)
Space Complexity - O(1) - if we ignore the return [list]
'''