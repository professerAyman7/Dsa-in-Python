# How to do it with 1 dict?

def compare(word1, word2):
    dict1 = {}
    dict2 = {}
    for char in word1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in word2:
        dict2[char] = dict2.get(char, 0) + 1

    return dict1 == dict2