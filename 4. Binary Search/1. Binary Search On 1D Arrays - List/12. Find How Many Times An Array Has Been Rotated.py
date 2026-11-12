class Solution:
    def arrayRotated(self, nums):
        n = len(nums)
        low = 0
        high = n - 1

        minNumber = float("inf")
        index = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= nums[high]:
                if nums[low] < minNumber:
                    minNumber = nums[low]
                    index = low
                low = mid + 1
            else:
                if nums[mid] < minNumber:
                    minNumber = nums[mid]
                    index = mid
                high = mid - 1

        return index


s = Solution()
# nums = [9,10,14,1,2,4,5,7,8]
# nums = [4, 5, 7, 8, 9, 10, 14, 1, 2]

# Here the minimum is at 0 so it returned 0 telling that the array is not rotated i thought it would return -1
nums = [1,2,4,5,7,8,9,10,14]
print(s.arrayRotated(nums))


'''
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''





