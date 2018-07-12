import re, sys

text = sys.stdin.read()
regex = r'(//.*?$|/\*.*?\*/)'
comments = re.findall(regex, text, re.MULTILINE|re.DOTALL)
for line in comments:
    print(re.sub('\n\s+', '\n', line))

