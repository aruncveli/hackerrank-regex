import re

Regex_Pattern = r'(?<=<)\w+'
tags = set()
for _ in range(int(input())):
    Test_String = input()
    match = re.findall(Regex_Pattern, Test_String)
    for tag in match:
        tags.add(tag)
print(';'.join(sorted(tags)))

