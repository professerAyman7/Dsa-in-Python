# Optimal Solution
def mergeArray(array1, array2):
    n = len(array1)
    m = len(array2)

    left, right = n - 1, 0

    while left >= 0 and right < m:
        if array1[left] > array2[right]:
            array1[left], array2[right] = array2[right], array1[left]
        else:
            # Do we have to break??
            break
        left  -= 1
        right += 1

    array1.sort()
    array2.sort()
    print(array1)
    print(array2)

array1 = [1, 3, 5, 7]
array2 = [0, 2, 6, 8, 9]
mergeArray(array1, array2)

'''
Time  Complexity - O(n + m) + O(n log n) + o(m log m)
Space Complexity - O(1)
'''