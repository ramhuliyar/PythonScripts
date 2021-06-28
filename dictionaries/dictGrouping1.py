from collections import defaultdict

nums = ['one', 'two', 'three', 'four', 'five', 'four', 'three', 'six',
        'one', 'three', 'four', 'two', 'one', 'five']

d = {}

for num in nums:
    key = len(num)
    if key not in d:
        d[key] = []
    d[key].append(num)




d = {}

for num in nums:
    key = len(num)
    d.setdefault(key,[]).append(num)


d = defaultdict(list)
for num in nums:
    key = len(num)
    d[key].append(num)
print(d.keys())    


