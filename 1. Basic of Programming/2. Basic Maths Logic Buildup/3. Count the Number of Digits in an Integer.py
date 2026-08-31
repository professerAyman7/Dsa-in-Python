# What about negative and why not 0 in the log
from math import *
def countDigits(nums):
    if nums == 0:
        return 1
    return int(log10(nums)+1)

nums = int(input("Enter a number: "))
print(countDigits(nums))