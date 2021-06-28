from collections import defaultdict

wordList = []
with open('dictComprehension.py', 'r') as f:
    for line in f:
        for word in line.split():
            wordList.append(word)

d = defaultdict(int)
for word in wordList:
    d[word] = d[word] + 1

print(d)    
