# The constraints were given

def hashing(listOne, listTwo):
    frequencyDict = dict()
    for n in listOne:
        frequencyDict[n] = frequencyDict.get(n, 0) + 1
    for m in listTwo:
        if m in frequencyDict:
            print(f"{m} comes {frequencyDict[m]} times")
        else:
            print(f"{m} is not present in the list")

listOne = [5,3,2,2,1,5,5,7,5,10,0]
listTwo = [10,111,1,9,5,67,2,0]
hashing(listOne, listTwo)


'''
Time  Complexity - O(n+m) - n and m are the length of the list
Space Complexity - O(d)   - number of distinct characters/elements

Space Complexity - ???
'''