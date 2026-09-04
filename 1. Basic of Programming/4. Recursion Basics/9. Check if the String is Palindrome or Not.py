def palindrome(name, left, right):
    if left >= right:
        return True
    if name[left] != name[right]:
        return False
    return palindrome(name, left+1, right-1)
# name = "NitiN"
name = "nItin"
print(palindrome(name, 0, len(name)-1))

'''
Time  Complexity - O(n/2) - O(n)
Space Complexity - O(n/2) - stack space
'''