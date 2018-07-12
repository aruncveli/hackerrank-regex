import re

regex = r'^[A-Z]{5}\d{4}[A-Z]$'
for _ in range(int(input())):
    pan = input()
    if bool(re.match(regex, pan)):
        print('YES')
    else:
        print('NO')

