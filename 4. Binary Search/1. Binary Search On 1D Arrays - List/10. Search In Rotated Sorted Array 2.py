
class Solution:
    def sortedArray(self, nums, target):
        n    = len(nums)
        low  = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            else:
                if nums[low] == nums[mid] == nums[high]:
                    low  += 1
                    high -= 1
                    # Why did we wrote this because the program will continue using the old mid
                    continue

            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low  = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low  = mid + 1
        return False

s      = Solution()
nums   = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]
target = 1

print(s.sortedArray(nums, target))


'''
Time  Complexity - O(log 2 (N)) - Average case

Time  Complexity - O(n/2)       - Worst Case
for a list like this - [7,7,7,7,7,7,7,1,7,7,7,7,7,7]

Space Complexity - O(1) 
'''



