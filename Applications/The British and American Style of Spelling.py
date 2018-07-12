import re

text = ''
for _ in range(int(input())):
    text += input()
for _ in range(int(input())):
    word = input()
    regex = r'' + word[:-2] + '[sz]e'
    print(len(re.findall(regex, text)))

