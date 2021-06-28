nums = [1, 2, 3, 4, 5]

names = ['one', 'two', 'three', 'four', 'five']

d = dict(zip(nums,names))

d2 = {6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

d.update(d2)
while d:
    key, value = d.popitem()
    print(key,value)
