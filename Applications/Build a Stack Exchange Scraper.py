import re
import sys

regex = r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>'
fragment = sys.stdin.read()
matches = re.findall(regex, fragment, re.DOTALL)
for match in matches:
        print(';'.join(match))

