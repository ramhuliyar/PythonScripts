import re
with open('ldpNG_3.txt', 'r') as reader:
    contents = reader.read()

suiteList = []
testCaseList = []
#matches = re.findall('^Suite\s+(\w+)[\r\n]+([^\r\n]+)', contents)
matches = re.findall(r'^Suite\s+(\w+)[\s]+.*', contents, re.MULTILINE)
print(matches)
for match in matches:
    print(match)

