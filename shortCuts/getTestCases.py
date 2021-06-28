import re

rf = open('testcases.txt', 'r')
wf = open('testcasesList.txt', 'w')

pattern = re.compile(r'((?:^\d+\s+)(?P<testCase>(\w+)([:]{2})?(\w+)?\s))')
pattern_epipe_vprn = re.compile(r'(epipe|vprn)',re.I)

unique_lines = []
for line in rf.readlines():
    matches = pattern.search(line)
    if matches:
        if not "SuiteCleanup" in matches.group('testCase'):
            modified_line = pattern_epipe_vprn.sub("XXX",matches.group('testCase')).strip()
            if modified_line not in unique_lines:
                unique_lines.append(modified_line)
                wf.write(matches.group('testCase').strip())
                wf.write('\n')

rf.close()
wf.close()
        
rf = open('testcasesList.txt', 'r')

print(rf.read())
for line in rf.readlines():
    pass
    
