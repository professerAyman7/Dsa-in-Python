# Brute Solution - How sir did??
def rearrange(nums):
    n = len(nums)
    positive = []
    negative = []

    for num in nums:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)

    result = []
    p, q = 0, 0

    while p < len(positive) and q < len(negative):
        result.append(positive[p])
        result.append(negative[p])
        p += 1
        q += 1

    return result

nums = [5, 10, -3, -1, -10, 6]
print(rearrange(nums))