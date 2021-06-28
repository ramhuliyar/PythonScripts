import os

print(os.path)


def getInterfaceStats(*args, **kwargs):
    print(args)
    print(kwargs)


nums = ['a', 'b', 'c', 'd']
num_names = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
getInterfaceStats(*nums, **num_names)

for i in range(10):
    print(i)
    pass
