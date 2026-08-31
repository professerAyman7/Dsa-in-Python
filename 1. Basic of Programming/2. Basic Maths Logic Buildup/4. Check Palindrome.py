def palindrome(num):
    x = num
    reversedNumber = 0
    while num > 0:
        reversedNumber = (10 * reversedNumber)+(num % 10)
        num = num // 10
    return x == reversedNumber

num = int(input("Enter a number: "))
print(f"Is the number palindrome: {palindrome(num)}")

"""
Time  Complexity - O(log10(num)) - num is the number entered
Space Complexity - O(1)
"""