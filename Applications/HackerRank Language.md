## [HackerRank Language](https://www.hackerrank.com/challenges/hackerrank-language/problem)

#### Task

Every submission at HackerRank has a field called language which  indicates the programming language which a hacker used to code his solution. Sometimes, error-prone API requests can have an invalid language field.  Could you find out if a given submission has a valid language field or not?

#### Solution Pattern

```python
regex = r'[1-9]\d\d\d\d\s' + \
        '(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|' + \
        'ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART| GROOVY|OBJECTIVEC)'
```

