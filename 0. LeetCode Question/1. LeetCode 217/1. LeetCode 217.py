def seen(nums):
    setSeen = set()
    for num in nums:
        if num in setSeen:
            return True
        setSeen.add(num)
    return False