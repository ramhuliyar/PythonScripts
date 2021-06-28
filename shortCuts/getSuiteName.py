import re
import os
import sys

with open('ldpNG_3.txt', 'r') as reader:
    contents = reader.read()

pattern = re.compile(r'(^Suite)(\s+)(\w+)', re.M|re.I)

'''
#Below can be used to get the Suite Names

matches = pattern.finditer(contents)
for match in matches:
    modified_text = pattern.sub(r'\3', match.group(0))
    print(modified_text)
'''
suiteList = []
testCaseList = []
flag = False
for line in contents.split('\n'):
    if flag:
        if re.search('(SuiteSetup|SuiteCleanup|\d+[ms]|masterlog|test_console)', line):
            continue
        print(line)
        testCaseList.append(re.search(r'\d+\s+(\w+)', line).group(1))
        flag = False
        continue
    if re.search('Suite\s+(\w+)', line):
        suiteList.append(re.match(r'Suite\s+?(\w+)', line).group(1))
        flag = True

'''
for suite, testCase in zip(suiteList, testCaseList):
    print(suite)
    print(testCase)
for suite in suiteList:
    print(suite)
'''

for testCase in testCaseList:
    print(testCase + ' ', end='')
