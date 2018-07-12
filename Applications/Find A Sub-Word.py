import re

n = int(input())
sentences = ''
for _ in range(n):
    sentences = sentences + '\n' + input()
q = int(input())
for _ in range(q):
    Regex_Pattern = r'\B' + input() + '\B'
    match = re.findall(Regex_Pattern, sentences)
    print(len(match))

