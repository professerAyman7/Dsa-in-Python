def merge(interval):
    # How does it sort with respect to inner list
    interval.sort()
    ans = []
    n   = len(interval)
    for i in range(n):
        if len(ans) == 0 or ans[-1][1] < interval[i][0]:
            ans.append(interval[i]) 
        else:
            ans[-1][1] = max(ans[-1][1], interval[i][1])
    return ans

interval = [[1,3], [2,6], [8,9], [9,11], [8,10], [2,4], [15,18], [16,17]]
print(merge(interval))

'''
Time  Complexity - O(N logN) + O(N)
Space Complexity - O(N) or if we ignore the answer as we return it- O(1) 
'''