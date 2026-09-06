def check(nums):
    numberSet = set()

    for num in nums:
        numberSet.add(num)

    maxCount = 0

    for n in numberSet:

        if n-1 not in numberSet:
            count = 1

            while n+1 in numberSet:
                count += 1
                n     += 1

            maxCount = max(maxCount, count)

    return maxCount