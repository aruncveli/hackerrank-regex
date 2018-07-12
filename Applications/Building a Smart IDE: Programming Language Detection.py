import re, sys

text = sys.stdin.read()
c_regex = r'#include<'
java_regex = r'import java'
if bool(re.search(c_regex, text)):
    print('C')
elif bool(re.search(java_regex, text)):
    print('Java')
else:
    print('Python')

