# Brute Solution
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
        minValue = max(nums)
        maxValue = sum(nums)

        # Time Complexity - O(n * (maxValue - minValue))
        for x in range(minValue, maxValue + 1):
            countStudents = self.check(nums, x)
            # Why didnt we write "==" here
            if countStudents <= student:
                return x


s = Solution()
nums = [25, 46, 28, 49, 24]
student = 1

print(s.valid(nums, student))


"""
Time  Complexity - O(n * (maxValue - minValue))
Space Complexity - O(1)
"""
