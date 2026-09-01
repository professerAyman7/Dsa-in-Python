def store(givenList):
    frequencyMap = dict()
    for i in range(0, len(givenList)):
        if givenList[i] in frequencyMap:
            frequencyMap[givenList[i]] += 1
        else:
            frequencyMap[givenList[i]] = 1
    return frequencyMap

givenList = [5,6,7,7,1,9,111,1,1,5,1,1]
print(store(givenList))

'''
Time  Complexity - O(n)
Space Complexity - O(n)
'''