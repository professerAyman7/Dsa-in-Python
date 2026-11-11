
class Solution:
    def minimum(self, nums):
        n = len(nums)
        low = 0
        high = n - 1

        minNumber = float("inf")

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= nums[high]:
                # Why to check "nums[low]" we can direclty check for nums[mid] here also??
                minNumber = min(nums[low], minNumber)
                low = mid + 1
            else:
                minNumber = min(nums[mid], minNumber)
                high = mid - 1

        return minNumber


s = Solution()
# nums = [4,5,6,7,0,1,2]
# nums = [5, 6, 7, 1, 2, 3, 4]
nums = [3, 4, 5, 1, 2]
print(s.minimum(nums))


"""
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
"""
