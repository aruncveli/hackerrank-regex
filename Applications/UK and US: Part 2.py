import re

text = ''
for _ in range(int(input())):
    text += input() + '\n'
for _ in range(int(input())):
    uk_spelling = input()
    uk_us_spelling = re.sub('our', 'ou?r', uk_spelling)
    regex = r'\b' + uk_us_spelling + r'\b'
    print(len(re.findall(regex, text)))

