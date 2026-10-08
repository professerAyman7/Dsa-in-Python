# Better Solution
def longestConsecutiveSequence(nums):
    mySet = set(nums)
    count       = 0
    longest     = 0

    for num in mySet:
        if num - 1 not in mySet:
            count = 1

            while num + 1 in mySet:
                count += 1
                num   += 1
                
        longest = max(longest, count)
    return longest


nums = [1,99,101,98,2,5,3,100,1,1]
print(longestConsecutiveSequence(nums))


'''
Why not n^2 if the while loop is inside the for loop
Time  Complexity - O(N + N + N)
Space Complexity - O(N)
'''