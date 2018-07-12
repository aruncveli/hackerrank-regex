import re

Regex_Pattern = r'^[_\.]\d+[a-zA-Z]*_?$'
for _ in range(int(input())):
    username = input()
    match = bool(re.search(Regex_Pattern, username))
    if match:
        print('VALID')
    else:
        print('INVALID')

