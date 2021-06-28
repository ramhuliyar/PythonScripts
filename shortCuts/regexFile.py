import re

with open('temp.txt', 'r') as rf:
    pattern = re.compile('^Suite\s+(\w+)')
    matches = [ re.findall(pattern, line)
                    for line in rf if re.findall(pattern, line)]

string = ''
for match in matches:
    string = string + ' ' + ' '.join(match)
print(string)
