import matplotlib.pylab as plt
from collections import defaultdict
with open('popItem.py', 'r') as f:
    contents = f.read()

d = defaultdict(int)

for letter in contents:
    d[letter] += 1

keys = d.keys()
values = d.values()

x = range(1,31)

plt.bar(x, 31)
plt.xticks(x, keys)
plt.xlabel('Characters')
plt.ylabel('Count')

plt.show()
