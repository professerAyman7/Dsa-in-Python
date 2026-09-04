'''Not the correct code!!!'''

def palindrome(name, left, right):
    while left < right:
        if name[right] != name[right]:
            return False
        left  += 1
        right -= 1
    return True
# name = "Nitin"
name   = "natin"
answer = palindrome(name, 0, len(name)-1)
print(answer)


'''
Time  Complexity - O(n/2) - O(n)
Space Complexity - O(1)
'''