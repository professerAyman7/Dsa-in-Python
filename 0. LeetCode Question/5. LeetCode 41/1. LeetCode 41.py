def question(nums):
    mySet = set()

    for num in nums:
        mySet.add(num)

    for i in range(1, len(nums)+2):
        if i not in mySet:
            return i