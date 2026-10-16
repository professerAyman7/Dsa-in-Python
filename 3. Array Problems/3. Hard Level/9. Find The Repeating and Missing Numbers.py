# My Solution
def numbers(nums):
    n = len(nums)
    myDictionary = {}
    result       = [] 
    for num in nums:
        myDictionary[num] = myDictionary.get(num, 0) + 1

    for key, value in myDictionary.items():
        if value == 2:
            result.append(key)

    # Till n+1
    for i in range(1, n + 1):
        if i not in myDictionary:
            result.append(i)

    return result

nums = [3, 5, 4, 2, 1, 1]
print(numbers(nums))