'''The user varaible does change here'''

def extract(num):
    # The num here is the local function variable
    while num > 0:
        print(num % 10, end = " ")
        num = num // 10

num = int(input("Enter a number to extract its digit: "))
extract(num)

"""
Time  Complexity - O(nd) - d is the number of the digits
Space Complexity - O(1)
"""