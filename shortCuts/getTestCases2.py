import re

rf = open('testcasesList.txt', 'r')

pattern = re.compile(r'(?:^\d+\s+)(?P<testCase>\w+)([:]+)?(\w*)?',re.M)
pattern_epipe_vprn = re.compile(r'(epipe|vprn)', re.I)
#pattern = re.compile(r'(?P<testCase>srTe)')
contents = rf.read()
matches = pattern.finditer(contents)

unique_line = []
onlyFirstTestFlag = True
onlyFirstTestcases = []
for match in matches:
    testCase = match.group('testCase')
    if not "Suite" in testCase:
        modified_line = pattern_epipe_vprn.sub('XXX', testCase)
        if not modified_line in unique_line:
            unique_line.append(modified_line)
            if onlyFirstTestFlag:
                onlyFirstTestcases.append(match.group('testCase'))
                onlyFirstTestFlag = False
                
            #print(match.group('testCase'))
    else:
        onlyFirstTestFlag = True

for testcases in onlyFirstTestcases:
    print(testcases, end=' ')
