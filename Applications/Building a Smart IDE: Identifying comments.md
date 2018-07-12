## [Building a Smart IDE: Identifying comments](https://www.hackerrank.com/challenges/ide-identifying-comments/problem)

#### Task

Your task is to write a program, which accepts as input, a C or C++ or  Java program and outputs only the comments from those programs.

#### Solution Pattern

```python
regex = r'(//.*?$|/\*.*?\*/)'
```
