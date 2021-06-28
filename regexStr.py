import re
para = '''
Posterior Inference {Causal Impact}\n Average Cumulative\nActual 3.43 13.7\nPrediction (s.d.) 3.38 (0.02) 13.53 (0.08)\n95% CI [3.34, 3.42] [13.38, 13.68]\n\nAbsolute effect (s.d.) 0.04 (0.02) 0.17 (0.08)\n95% CI [0.01, 0.08] [0.02, 0.33]\n\nRelative effect (s.d.) 1.27% (0.57%) 1.27% (0.57%)\n95% CI [0.18%, 2.41%] [0.18%, 2.41%]\n\nPosterior tail-area probability p: 0.01\nPosterior prob. of a causal effect: 99.2%\n\nFor more details run the command: print(impact.summary('report'))
'''

pattern_actual = re.compile(r'Actual\s+(?P<Actual>\S+\s+\S+)')
pattern_absolute = re.compile(r'Absolute effect \(s\.d\.\)\s+(?P<Abs>\S+\s+\S+\s+\S+\s+\S+)')
match = re.search(pattern_actual,para)
print(match.group('Actual'))

match = re.search(pattern_absolute,para)
print(match.group('Abs'))

match = re.search('(?P<name>.*) (?P<phone>.*)', 'John 123456')
print(match.group('name'))

regex = re.compile(
    r"Actual\s(?P<actual_avg>-?\d+(?:\.\d+)?).*?"
    r"(?P<actual_cumul>-?\d+(?:\.\d+)?)\n.*?"
    r"Absolute effect \(s\.d\.\)\s(?P<abs_avg>-?\d+(?:\.\d+)?).*?"
    r"\(.*?\).*?(?P<abs_cumul>-?\d+(?:\.\d+)?).*?"
    r"Relative effect \(s\.d\.\)\s(?P<relative_avg>-?\d+(?:\.\d+)?)%.*?"
    r"\(.*?\).*?(?P<relative_cumul>-?\d+(?:\.\d+)?)%.*?"
, re.DOTALL)

regex = re.compile(
    r"Actual\s(?P<actual_avg>\d+(?:\.\d+)?)?"
, re.DOTALL)

matches = re.finditer(regex,para)
for match in matches:
    for items in match.groupdict():
        print(items, match.groupdict()[items])
