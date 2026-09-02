# The constraints were given
# How sir did???

def hashing(character, listTwo):
    frequencyDict = dict()
    for n in character:
        frequencyDict[n] = frequencyDict.get(n, 0) + 1
    for m in listTwo:
        if m in frequencyDict:
            print(f"{m} comes {frequencyDict[m]} times")
        else:
            print(f"{m} is not present in the list")

character = "azyxyyzaaaaD"
listTwo = ["d", "a", "y", "x", "D"]
hashing(character, listTwo)

'''
Time  Complexity - O(n+m) - n and m are the length of the list
Space Complexity - O(d)   - number of distinct characters/elements

Space Complexity - ???
'''