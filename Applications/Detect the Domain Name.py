import re

regex = r'https?://(?:ww[w2]\.)?([a-zA-Z\d-]+(?:\.[a-zA-Z\d-]+)+)'

text = ''
for _ in range(int(input())):
    text += input() + '\n'
matches = re.findall(regex, text)
print(';'.join(sorted(set(matches))))

