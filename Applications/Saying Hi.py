import re

regex = r'^[hH][iI]\s[^dD]'
for _ in range(int(input())):
    line = input()
    if bool(re.search(regex, line)):
        print(line)

