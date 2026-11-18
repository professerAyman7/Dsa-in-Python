
class Solution:
    def nthRoot(self, n, m):
        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2

            if (mid**n) == m:
                return mid

            elif (mid**n) < m:
                low = mid + 1

            else:
                high = mid - 1

        return -1


s = Solution()
n = 3
m = 125
print(s.nthRoot(n, m))


"""
Time  Complexity - O(log 2 (N))
Space Complexity - O(1)
"""



