import re

regex = r'\b(?:\w|\.)+@(?:\w*\.*)+\b'
text = ''
for _ in range(int(input())):
    text += input() + '\n'
matches = re.findall(regex, text)
print(';'.join(sorted(set(matches))))

