# Print your name 4 times using recursion
'''Head Recursion!!! - First we will do the work then we will do the call'''

def recursion(i):
    if i == 4:
        return
    print("Ayman")
    recursion(i+1)

recursion(0)

'''
Time  Complexity - O(n) - The number of times the recursive function is called.
Space Complexity - O(n) - Stack space
'''