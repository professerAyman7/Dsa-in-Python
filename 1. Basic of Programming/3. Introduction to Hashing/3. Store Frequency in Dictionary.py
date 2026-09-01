def store(givenList):
    hashMap = dict()
    for i in range(0, len(givenList)):
        hashMap[givenList[i]] = hashMap.get(givenList[i], 0) + 1
    return hashMap
    

givenList = [5,6,7,7,1,9,111,1,1,5,1,1]
print(store(givenList))


'''
Time  Complexity - O(n)
Space Complexity - O(n)
'''