
# Brute Solution
class Solution:
    def singleElement(self, nums):
        n = len(nums)

        # Edges Cases
        if nums[0] != nums[1]:
            return nums[0]

        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        # For rest of the elements
        for i in range(1, n-1):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]

s    = Solution()
nums = [1,1,2,2,4,4,6,7,7,8,8]

print(s.singleElement(nums))


'''
Time  Complexity  - O(n-2) but we ignore the constant so O(n)
Why O(n-2) we did - because in the starting we checked for the starting and ending number so we removed them but we ignore the constant so O(n)

Space Complexity - O(1)
'''




