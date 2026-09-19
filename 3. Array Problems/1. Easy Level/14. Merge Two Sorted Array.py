def sorted(nums1, nums2):
    n = len(nums1)
    m = len(nums2)

    i,j = 0,0
    result = []

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    return result

nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

print(sorted(nums1, nums2))


'''
Time  Complexity - O(n + m) - n and m are the length of the arrays
Space Complexity - O(1) - if we ignore the result space otherwise it will be O(n + m)
'''