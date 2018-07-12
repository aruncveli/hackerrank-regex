import re

regex = r'(^\d{1,3}[- ]\d{1,3}[- ]\d{4,10})$'
for _ in range(int(input())):
    number = input()
    if bool(re.search(regex, number)):
        match = list(re.split('\s|-', number))
        print('CountryCode=' + match[0] + ',LocalAreaCode=' + match[1] + ',Number=' + match[2])

