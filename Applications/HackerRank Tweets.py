import re

regex = r'[hH][aA][cC][kK][eE][rR][rR][aA][nN][kK]'
count = 0
for _ in range(int(input())):
    text = input()
    if bool(re.search(regex, text)):
        count += 1
print(count)

