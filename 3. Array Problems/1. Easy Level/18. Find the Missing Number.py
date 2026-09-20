# My thinking!!!

def missing(nums):
    # This also takes O(n)
    setNumber = set(nums)

    # O(n)
    for i in range(0, len(nums)+1):
        if i not in setNumber:
            return i

nums = [1,0,3,2]
print(missing(nums))


'''
Time  Complexity - O(n+n) - O(2n) - O(n)
Space Complexity - O(n) - creation of set
'''