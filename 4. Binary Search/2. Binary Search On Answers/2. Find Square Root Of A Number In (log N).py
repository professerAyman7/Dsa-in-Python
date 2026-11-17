
class Solution:
    def squareRoot(self, number):
        low    = 1
        high   = number

        while low <= high:
            mid = (low + high) // 2

            if (mid * mid) <= number:
                low = mid + 1
            else:
                high = mid - 1

        # Why do we return high - cause when low and high cross each other high contains that correct answer 
        return high


s = Solution()
number = 110
print(s.squareRoot(number))


'''
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
'''


