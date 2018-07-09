## [Positive Lookbehind](https://www.hackerrank.com/challenges/positive-lookbehind/problem)

#### Task

You have a test String ***S***. 

Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.

#### Solution

```python
Regex_Pattern = r"(?<=[13579])\d"
```

