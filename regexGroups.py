import re

'''
Nuances with Groupings
'''

string = 'ababababab'
match = re.search('(ab)+',string)   ;#Groups are overwritten
print(match.group(0), match.group(1))

string = 'abababababab'
# Same matching group moves back one step or matching.
# Groups keep updated multiple times and the group value is overwritten
match = re.search('((ab)+)(ab)+', string)
print(match.group(0), match.group(1), match.group(2))

string = "Happy Valentine's"
#Grouping of words for neatness. Groups for word completion
pattern = re.compile('Happy (Birthday|Valentine\'s)')
match = re.search(pattern, string)
print(match)

'''
(?:regex) - Non capturing groups
(?P<>regext) - Group naming.

When we capture groups we are either storing the value or
outputting them

Back referencing is used to check for the SAME thing as the previous
match. 
'''
