import re

IPv4 = r'^((25[0-5]|2[0-4]\d|[01]\d\d|\d\d|\d)\.){3}(25[0-5]|2[0-4]\d|[01]\d\d|\d\d|\d)$'
IPv6 = r'^([0-f]{1,4}:){7}[0-f]{1,4}$'
for _ in range(int(input())):
    text = input()
    if bool(re.search(IPv4, text)):
        print('IPv4')
    elif bool(re.search(IPv6, text)):
        print('IPv6')
    else:
        print('Neither')

