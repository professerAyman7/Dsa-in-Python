# The constraints were given

def hashing(listOne, listTwo):
    # hashList = [0 for i in range(0, 11)]
    hashList = [0] * 11
    for n in listOne:
        hashList[n] += 1
    for m in listTwo:
        if m >= 0 and m < 11:
            print(f"{m} comes {hashList[m]} times.")
        else:
            print(f"{m} is not present in the list")

listOne = [5,3,2,2,1,5,5,7,5,10,0]
listTwo = [10,111,1,9,5,67,2,0]
hashing(listOne, listTwo)

'''
Time  Complexity - O(n+m) - n and m are the length of the lists
Space Complexity - O(11)  - O(1) always constant
'''