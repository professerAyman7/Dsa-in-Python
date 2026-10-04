# Optimul Solution - Moore's Voting Algo - whats the logic behind this algo??

def majority(nums):
    n = len(nums)
    count = 0
    element = None

    for i in range(0, n):
        if count == 0:
            element = nums[i]
            count += 1
        elif nums[i] == element:
            count += 1
        else:
            count -= 1

    return element

    '''
    if the solution doesnt exist
    count = 0
    for i in range(0, n):
        if nums[i] == element:
            count += 1
    if count > n // 2:
        return element
    return - 1
    '''

nums = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority(nums))


'''
Time  Complexity - O(n)
Space Complexity - O(1)
'''