import re
string = '''Lionel D Messi: F 
Cristiano Ronaldo: F 
NGolo Kante: M 
Ruben Dias: D    
Toni K Kroos: M 
Sergio Ramos: D 
Paul Pogba: M 
Marcus Rashford: F 
Harry Kane: F 
Manuel Neuer G 
David DeGea: G
'''

midFielders = re.compile(r'^(\w+\s+(?:\w+\s+)?\w+):\s+(?!M)', re.M)
#midFielders = re.compile(r'^(.*?)',re.DOTALL)
match = re.findall(midFielders,string)
print(match)

text = 'This is a large subsring. bla bla bla AND www.dumbweb.com/Dumbo and www.otherLinks.com...'

pattern = '(\S*(?=dumbweb.com)\S*)'

theLink = re.findall(pattern, text)

print(theLink)
