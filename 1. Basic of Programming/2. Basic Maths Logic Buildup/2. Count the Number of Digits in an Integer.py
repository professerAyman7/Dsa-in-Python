# What about negative?
def countDigits(nums):
    count = 0
    if nums == 0:
        return 1
    while nums > 0:
        count += 1
        nums = nums // 10
    return count

nums = int(input("Enter a number: "))
print(countDigits(nums))

"""
Time  Complexity - O(log10(nums)) - nums is the number
Space Complexity - O(1)
"""