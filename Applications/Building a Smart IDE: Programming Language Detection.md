## [Building a Smart IDE: Programming Language Detection](https://www.hackerrank.com/challenges/programming-language-detection/problem)

#### Task

We are trying to hack together a smart programming IDE. Help us build a  feature which auto-detects the programming language, given the source  code.  There are only three languages which we are interested in  "auto-detecting": Java, C and Python.

#### Solution Pattern

```python
c_regex = r'#include<'
java_regex = r'import java'
```

This is a very trivial and a sort of a *hack* to this task, which however passes the test cases.

In a scenario where we include a Java code snippet inside a C code as comments, this hack fails.

If we have the source code files with us, the solution is to just look at the file extension. If we do not have access to the files, the best solution to this problem will be to model this as a NLP classification problem.