
# Optimal Solution
class Solution:
    def singleElement(self, nums):
        n    = len(nums)

        # Edge Cases
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        # For rest of the elements
        low  = 1
        high = n - 2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]

            # Why did we wrote these cases now did u understand?
            if nums[mid] == nums[mid+1]:
                if (mid % 2) != 0:
                    high = mid - 1
                else:
                    low  = mid + 1

            else:
                if (mid % 2) != 0:
                    low  = mid + 1
                else:
                    high = mid - 1

s    = Solution()
nums = [1,1,2,2,4,4,6,7,7,8,8]

print(s.singleElement(nums))


'''
Time  Complexity - O(log 2 (N - 2)) but we ignore the constant so O(log 2 (N))
Why O(log 2 (n-2)) we did - because in the starting we checked for the starting and ending number so we removed them but we ignore the constant so   O(log 2 (n))

Space Complexity - O(1)
'''

