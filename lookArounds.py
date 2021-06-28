import re

string = '''
        ABC1     1.1.1.1     sdfkjsafdr    active
        ABC32    2.2.2.2     p32sffwaff    inactive
        ABC1     x.x.x.x     sdfkjsafdr    active
        '''
'''
pattern = re.compile('ABC\w+\s+(\S+)\s+\S+\s+(?=active)\S+',re.MULTILINE)

print(re.findall(pattern,string))
matches = re.finditer(pattern,string)

for match in matches:
    print(match.groups())
'''

string = 'abababacb'

pattern = re.compile('(?:b)(a)(?:b)')

print(re.findall(pattern,string))

pattern = re.compile('(?=(bab))')

print(re.findall(pattern,string))

string = 'I love cherries, apples, and strawberries.'

pattern = re.compile('\w+(?=[\.,])')

print(re.findall(pattern,string))

# Consecutive Look Around Fallacy

string = '''Cherry 100 red
            Apple 150 green
            Grapes 100
         '''

pattern = re.compile('\w+\s+(?=\d+\s+\w+)')
print(re.findall(pattern,string))
      

#Negative Look Arounds

string = '''
Full Invitation List:

Guest: Ashely Jackson
Guest: Maria Maria Jackson
Guest: Bob Sanders
Guest: Bill Smith
Entertainer: Michael Johnson
Baker: Chris Jackson
Party Planner: Seema Patel
Publicist: Seema Patel
Baker: Ashley Sanders
'''

pattern = re.compile(r'(?<!Baker: )\b\w+\s+(?:\w+\s+)?\w+$',re.I|re.M)
print(re.findall(pattern,string))


pattern = re.compile(r'^(?!Baker: ).+\w+$',re.I|re.M)
print(re.findall(pattern,string))

import regex

string = '''
        1111    ABC     1.1.1.1     sdfkjsafdr    active
        bbbb    ABC    2.2.2.2     p32sffwaff    inactive
        3333    ABC23     x.x.x.x     sdfkjsafdr    active
        '''
#pattern = regex.compile('(?<=\d+\w+)[0-9]+\s+[A-Z0-9]+\s+(\S+)')
pattern = re.compile(r'(?<=\d+\s+[A-Z]+).*')
print(re.findall(pattern,string))
