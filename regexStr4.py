import re

string = '''https://ci.adoptopenjdopenjdktest_s390x_linux/18/consoleFull
https://ci.adoptopenjd3452/k11_hs_sanity.openjdk_x86-64_mac/26/consoleFull
To reproduce: https://ci.adnjdk14_hs_sanity.openjdk_ppc64_aix/111/console
Jenkins Build URL: https://_openjdk8_hs_extended.system_ppc64le_linux/259/
internal build Test_openjdj9_sanity.openjdk_aarch64_linux/43/
internal build Test_openjdk11_j9_sanity.functional_aarch64_linux/46
'''

'''
pattern = re.compile(r'((https:|http:|ftp:)\/\/ci\.adoptopenjdk\.net.+\/)')

matches = re.findall(pattern, string)

for match in matches:
    print(match[0])
'''
numLines = 3

pattern = re.compile(r'(?P<FirstCapLines>(.*\n){3})(?P<AfterCapLines>[\s\S]*)')

match = re.search(pattern,string)

print(match.group('FirstCapLines'))
print(match.group('AfterCapLines'))

                     
