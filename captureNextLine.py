import re
string = '''Hello
            World
            Universe
            Earth
        '''
match = re.search('World\n([^\r\n]+)', string).group(1).strip()

nums = ['One\n', 'two\n', 'three\n']
print(''.join(nums))
new_nums = list(num.rstrip('\n') for num in nums)
print(' '.join(new_nums))
