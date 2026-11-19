
# Brute Solution
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
        
        minDays = min(bloomdays)
        maxDays = max(bloomdays)

        # Time Complexity - O((max - min) * n)
        for x in range(minDays, maxDays + 1):

            if self.bloom(m, k, x, bloomdays) == True:
                return x
            
        return -1

s = Solution()
m = 2
k = 3
bloomdays = [8,8,8,8,13,11,12,7]

print(s.answer(m, k, bloomdays))


'''
Time  Complexity - O((max - min) * n)
Space Complexity - O(1)
'''
