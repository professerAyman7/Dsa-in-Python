# Optimal Solution
class Solution:
    def check(self, nums, x):
        studentRequired = 1
        currentPages = 0

        # Time Complexity - O(n)
        for pages in nums:
            if currentPages + pages > x:
                studentRequired += 1
                currentPages = pages
            else:
                currentPages += pages
        return studentRequired

    def valid(self, nums, student):
        # Ignoring these Time Complexity
        low = max(nums)
        high = sum(nums)

        # Time Complexity - O(n * log 2 (maxValue - minValue))
        while low <= high:
            mid = (low + high) // 2

            countStudents = self.check(nums, mid)
            if countStudents <= student:
                high = mid - 1
            else:
                low = mid + 1
        return low


s = Solution()
nums = [25, 46, 28, 49, 24]
student = 4

print(s.valid(nums, student))


"""
Time  Complexity - O(n * log 2 (maxValue - minValue))
Space Complexity - O(1)
"""

