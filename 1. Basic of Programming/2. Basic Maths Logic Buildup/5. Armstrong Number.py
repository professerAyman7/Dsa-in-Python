def armstrong(num):
    n = num
    # Does calculating len also takes complexity?
    length = len(str(num))
    total  = 0
    while num > 0:
        total = total + ((num % 10) ** length)
        num //= 10
    return n == total

num = int(input("Enter a number: "))
print(f"Is the given number armstrong: {armstrong(num)}")

'''
Time  Complexity - O(log10 N) - n is the number entered
Space Complexity - O(1)
'''