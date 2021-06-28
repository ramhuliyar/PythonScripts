
colors = ['voilet', 'indigo', 'blue', 'green', 'yellow', 'voilet', 'blue']

d = {}

for color in colors:
    if color not in d:
        d[color] = 1
    else:
        d[color] += 1

print(d)        

d = {}

for color in colors:
    d[color] = d.get(color, 0) + 1
    print(d.get(color))

print(d)

