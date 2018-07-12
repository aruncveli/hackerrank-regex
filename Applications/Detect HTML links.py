import re

link_and_text = r'<a href=\"(.*?)\".*?>([\w ,./]*)(?=</)'
for _ in range(int(input())):
    line = input()
    match = re.findall(link_and_text, line)
    for link, text in match:
        print(link + ',' + text.strip())

