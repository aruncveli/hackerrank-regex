import re

text = ''
for _ in range(int(input())):
    text += input() + '\n'
for _ in range(int(input())):
    word = input()
    regex = r'\b' + word + r'\b'
    matches = re.findall(regex, text)
    count = len(matches)
    print(count)

