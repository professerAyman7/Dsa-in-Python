def recursion(num, left, right):
    if left > right:
        return
    num[left], num[right] = num[right], num[left]
    recursion(num, left+1, right-1)

num = [5,7,3,2,6,1,5,9]
recursion(num, 0, len(num)-1)
print(num)


'''
Time  Complexity - O(n/2) - O(n)
Space Complexity - O(n/2) - O(n)
'''