
class Solution:
    def peakElement(self, nums):
        n = len(nums)

        # From where does it start!
        low = 1
        high = n - 2

        while low <= high:
            # Edge Cases
            if n == 1:
                return 0

            if nums[0] > nums[1]:
                return 0

            if nums[n - 1] > nums[n - 2]:
                return [n - 1]

            mid = (low + high) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            # Deciding the slope where we have to go!!
            if nums[mid - 1] >= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1


s = Solution()
nums = [5, 7, 8, 10, 4, 3, 2, 7, 5, 4, 1]
print(s.peakElement(nums))


'''
Time  Complexity - O(log 2 (N - 2)) but we ignore the constant so O(log 2 (N))
Why O(log 2 (n-2)) we did - because in the starting we checked for the starting and ending number so we removed them but we ignore the constant so   O(log 2 (n))

Space Complexity - O(1)
'''

