
class Solution:
    def first(self, nums, target):
        n    = len(nums)
        low  = 0
        high = n

        first = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                first = mid
                high  = mid - 1
            else:
                low  = mid + 1
        
        return first

    def last(self, nums, target):
        n    = len(nums)
        low  = 0
        high = n - 1
    
        last = n
    
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                last = mid
                high = mid - 1
            else:
                low  = mid + 1
    
        return last 

    def countOccurrence(self, nums, target):
        first = self.first(nums, target)
        
        if first == -1 or nums[first] != target:
            return [-1, -1]
                    
        last  = self.last(nums, target)
        
        return last - first

s        = Solution()
nums     = [1,2,3,3,3,3,3,5,6,8,9,9,10,10]
nums     = [1]
target   = 1

print(s.countOccurrence(nums, target))


'''
n is the number of elements in the list

Time  Complexity - O(2(log 2 (N))) - O(log 2 (N))
Space Complexity - O(1)
'''




