import re

regex = r'[1-9]\d\d\d\d\s' + \
        '(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|' + \
        'ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART| GROOVY|OBJECTIVEC)'
for _ in range(int(input())):
    line = input()
    if bool(re.search(regex, line)):
        print('VALID')
    else:
        print('INVALID')

