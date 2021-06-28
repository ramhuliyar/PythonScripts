import re

text_to_search = ''' Regular Expressions Basics

    1. Always safer to use raw strings (r'' | r"").
        Tells Python not to handle special characters in any way
        And rather pass the string as it is to the objects
        r'' on patterns doesn't have any impact
    2. re.match() matches starting at the beginning of a string
       and upto \n. It does not go to next lines in the string. 
    3. re.search() matches first occurance of the pattern anywhere
       in the string. Even \n in the string will result in the search
    4. match and search returns None if no match else Objects.
    5. Retrieve captured matches via group method on the match object.
    6. re.findall() all matches to a pattern. Returns list of match objects.
       Outputs the group captures. If multiple then as tuples. 
    7. With captured expressions re.findall() returns list of tuples,
       the tuples being the captures.
    8. re.sub(). Replaces all instances of a pattern by default.
       Use max parameter to specify number of instance to replace.
    9. To make re.search() case insensitive re.I as final argument.
    10. re.compile(); Convert patters into a variable and reuse it across
        many times.
    11. re.finditer(), Good tool for finding matches and gets more information
    12. re.compile(pattern, re.IGNORECASE|re.MULTILINE)

. \d, \D, \w, \W, \s, \S - Metachars
\b, \B, ^, $ - Boundary
[], [^], Characters in the bracket; ^ inverse and - between characters.
* ,+, ? {3} {3,4} are quantifiers

MetaCharacters: . ^ $ * + ? {} [] | \ ()

Mr. Tab
Mr Shah
Mr. B
Mrs. Kelly Woll
Mrs Taara
Ms Rita Raf

800-666-2222
900-666-2222

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov


'''

sentence = "Start a sentence and then bring it to an end"

re.search('Start', sentence).group()
re.match('Start', sentence).group()

bool(re.match('Start', sentence).group())   ;#None when match is fail.

#pattern = re.compile(r'(\w+)(se)(?:\w+)?')
#pattern = re.compile(r'(^Start)')
#pattern = re.compile(r'(\d{3})[-.](\d{3})[-.](\d{4})')
#pattern = re.compile(r'[89]00[-.](\d{3})[-.](\d{4})')
#pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*( [A-Z]\w*)')

pattern = re.compile(r'https?://(www.)?([A-Za-z0-9_.-]+)(\.(com|gov))')

subbed_urls = pattern.sub(r'\2\3', text_to_search)
print(subbed_urls)
#print(text_to_search)

matches = pattern.finditer(text_to_search)
#matches = pattern.finditer(sentence)

for match in matches:
    #print(type(match))
    #print(dir(match))
    #print(len(match.groups()))
    #print(match.group(2))
    print(f'{match.group(2)}{match.group(3)}')

'''
with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
        a, b = match.span()
        print(contents[a:b])
'''    


