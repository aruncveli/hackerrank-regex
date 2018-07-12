import re

regex = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'
for _ in range(int(input())):
    number = input()
    if bool(re.match(regex, number)):
        print('VALID')
    else:
        print('INVALID')

