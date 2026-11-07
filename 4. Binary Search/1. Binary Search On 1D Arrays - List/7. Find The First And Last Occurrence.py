
class Solution:
    def lowerBound(self, nums, target):
        n     = len(nums)
        low   = 0
        high  = n - 1

        first = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                first = mid
                high  = mid - 1
            else:
                low  = mid + 1

        return first

    def upperBound(self, nums, target):
        n    = len(nums)
        low  = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                last = mid
                high = mid - 1
            else:
                low  = mid + 1

        return last 

    def answerFunction(self, nums, target):
        first = self.lowerBound(nums, target)

        # I think first will never be -1
        if first == -1 or nums[first] != target:
            return [-1, -1]
            
        last  = self.upperBound(nums, target)

        return [first, last - 1]
    
s = Solution()
nums   = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 7

print(s.answerFunction(nums, target))


'''
n is the number of elements in the list

Time  Complexity - O(2(log 2 (N))) - O(log 2 (N))
Space Complexity - O(1)
'''

