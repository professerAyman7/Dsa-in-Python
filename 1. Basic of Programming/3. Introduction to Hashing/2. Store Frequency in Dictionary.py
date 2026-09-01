# Return how many times a number is repeated!!

def store(givenList, x):
    frequencyMap = dict()
    for i in range(0, len(givenList)):
        if givenList[i] in frequencyMap:
            frequencyMap[givenList[i]] += 1
        else:
            frequencyMap[givenList[i]] = 1
    if x in frequencyMap:
        return frequencyMap[x]
    else:
        return 0

givenList = [5,6,7,7,1,9,111,1,1,5,1,1]
x = int(input("Enter number to check: "))
print(store(givenList, x))