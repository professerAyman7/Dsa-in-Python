# Better Solution
def longestConsecutiveSequence(nums):
    nums.sort()
    lastSmaller = float("-inf")
    count       = 0
    longest     = 0

    for num in nums:
        if (num-1) == lastSmaller: 
            count += 1
            lastSmaller = num
        elif num == lastSmaller:
            continue
        else:
            count = 1
        lastSmaller = num
        longest = max(longest, count)

    return longest

nums = [1,99,101,98,2,5,3,100,1,1]
print(longestConsecutiveSequence(nums))


'''
Time  Complexity - O(Nlog N + N)
Space Complexity - O(1)
'''