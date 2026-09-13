# Better Soluion

def secondLargest(nums):
    largestNumber = float("-inf")
    secondLargestNumber = float("-inf")

    for num in nums:
        if num > largestNumber:
            largestNumber = num

    for num in nums:
        if num > secondLargestNumber and num != largestNumber:
            secondLargestNumber = num

    return f"The second largest number is {secondLargestNumber}"

nums = [55,32,97,-55,45,32,88,21]
print(secondLargest(nums))


'''
Time  Complexity - O(n+n) - O(2n) - O(n)
Space Complexity - O(1)
'''