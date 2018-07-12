import re

regex = r'^\(' + \
        '[-+]?(([1-8]?[0-9]|0)(\.\d+)?|90(\.0+)?),' + '\s' + \
        '[-+]?((1?[1-7]?[0-9]|10[0-9]|[1-9][0-9]|0)(\.\d+)?|180(\.0+)?)' + \
        '\)$'
for _ in range(int(input())):
    text = input()
    if bool(re.search(regex, text)):
        print('Valid')
    else:
        print('Invalid')

