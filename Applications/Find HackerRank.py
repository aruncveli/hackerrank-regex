import re

start = r'^hackerrank'
end = r'hackerrank$'
start_end = r'^(hackerrank|(hackerrank.*?hackerrank))$'
for _ in range(int(input())):
    conv = input()
    if bool(re.search(start_end, conv)):
        print(0)
    elif bool(re.search(start, conv)):
        print(1)
    elif bool(re.search(end, conv)):
        print(2)
    else:
        print(-1)

