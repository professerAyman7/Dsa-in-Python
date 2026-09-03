'''Tail Recursion!!! - We will first call then we will do the work'''

def recursion(i):
    if i == 4:
        return
    recursion(i+1)
    print("Ayman")

recursion(0)

'''
Time  Complexity - O(n) - The number of times the recursive function is called.
Space Complexity - O(n) - Stack space
'''