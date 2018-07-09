## [Backreferences To Failed Groups](https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem)

#### Task

You have a test string ***S***. 

Your task is to write a regex which will match ***S***, with following condition(s):

- ***S*** consists of 8 digits. 
- ***S*** may have "***-***" separator such that string ***S*** gets divided into ***4*** parts, with each part having exactly two digits. (Eg. *12-34-56-78*)

#### Solution

```python
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"
```

