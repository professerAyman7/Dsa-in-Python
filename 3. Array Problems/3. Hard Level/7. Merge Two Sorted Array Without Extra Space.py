# Brute Solution - Using extra space
def mergeArray(array1, array2):
    n = len(array1)
    m = len(array2)

    array3 = [0] * (n * m)
    left   = 0
    right  = 0
    index  = 0

    # Merging two sorted array into one
    while left < n and right < m:
        if array1[left] <= array2[right]:
            array3[index] = array1[left]
            left  += 1
            index += 1
        else:
            array3[index] = array2[right]
            right += 1
            index += 1
    # If right pointer reaches the end
    while left < n:
        array3[index] = array1[left]
        left  += 1
        index += 1
    # If left pointer reaches the end
    while right < m:
        array3[index] = array2[right]
        right += 1
        index += 1

    # Placing them into the original arrays
    for i in range(n + m):
        if i < n:
            array1[i] = array3[i]
        else:
            array2[i - n] = array3[i]

    print(array1)
    print(array2)

array1 = [1, 3, 5, 7]
array2 = [0, 2, 6, 8, 9]
mergeArray(array1, array2)

'''
Time  Complexity - O(n + m) + O(n + m) - O(2(n + m)) - O(n + m)
Space Complexity - O(n + m)
'''