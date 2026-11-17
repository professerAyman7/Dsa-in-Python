
# Brute Solution
class Solution:
    def squareRoot(self, number):
        answer = 0
        for i in range(1, number + 1):
            if i * i <= number:
                answer = i
            else:
                break

        return answer


s = Solution()
number = 36
print(s.squareRoot(number))


"""
Time  Complexity - O(n)
Space Complexity - O(1)
"""

