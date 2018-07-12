import re
from collections import defaultdict

tag_regex = r'<(\w+)(|\s+[^>]*)>'
attribute_regex = r'\w+(?==[\'\"])'
attribute_dict = defaultdict(list)
for _ in range(int(input())):
    line = input()
    matches = re.findall(tag_regex, line)
    for tag, attributes in matches:
        attributes_list = re.findall(attribute_regex, attributes)
        attribute_dict[tag].extend(attributes_list)
for tag in sorted(attribute_dict.keys()):
    print(tag + ':' + ','.join([i for i in sorted(set(attribute_dict[tag]))]))

