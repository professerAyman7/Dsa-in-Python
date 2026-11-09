
class Solution:
    def searchRotated(self, nums, target):
        n    = len(nums)
        low  = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low  = mid + 1
                else:
                    high = mid - 1

            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low  = mid + 1
        return -1

s      = Solution()
nums   = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target = 20

print(s.searchRotated(nums, target))


'''
Note - why did we use ">=" or "<=" why didnt we use ">" or "<"
n is the number of elements in the list

Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''




