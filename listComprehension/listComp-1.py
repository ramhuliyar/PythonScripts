''' Three parts to list comprehension
1. the loop
2. the transformation
3. filtering
'''

mylist = [1, 2, 3, 4, 5]

modlist = []

for i in mylist:
    j = i * 2
    modlist.append(j)

print(modlist)    

mylist = [100, 200, 300, 400, 500]
r, t = 10, 1

#modlist = [lambda p: p*t*r/100 for p in mylist]

#print(modlist)

line = [line.strip() for line in open('listComp-1.py')
        if not line.startswith('#')]
print(line)


