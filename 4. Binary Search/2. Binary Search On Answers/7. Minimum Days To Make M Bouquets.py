
# Optimal Solution
class Solution:
    def bloom(self, m, k, day, bloomdays):

        count = 0
        total = 0

        # Time Complexity - O(n)
        for x in bloomdays:
            if day >= x:
                count += 1

                if count  == k:
                    total += 1
                    count  = 0
            else:
                count = 0

        return total >= m

    
    def answer(self, m, k, bloomdays):

        if (m * k) > len(bloomdays):
            return -1
         
        low     = min(bloomdays)
        high    = max(bloomdays)

        returnAnswer = -1

        # Time Complexity - O(log 2 (high - low))
        while low <= high:
            mid = (low + high) // 2

            if self.bloom(m, k, mid, bloomdays) == True:
                returnAnswer = mid
                high = mid - 1
            else:
                low  = mid + 1

        return returnAnswer

s = Solution()
m = 2
k = 3
bloomdays = [8,8,8,8,13,11,12,7]

print(s.answer(m, k, bloomdays))


'''
Time  Complexity - O(n * (log 2 (high - low)))
Space Complexity - O(1)
'''



