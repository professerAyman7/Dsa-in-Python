def largest(nums):
    largest = float("-inf")

    for num in nums:
        if num > largest:
            largest = num

    return largest

nums = [55,32,-97,99,3,67]
print(f"The largest element is: {largest(nums)}")


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''