def targets(nums, target):
    dictValue = {}
    for i in range(0, len(nums)):
        find = target - nums[i]

        if find in dictValue:
            return [dictValue[find], i]
        
        dictValue[nums[i]] = i