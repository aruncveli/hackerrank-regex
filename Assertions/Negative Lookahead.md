## [Negative Lookahead](https://www.hackerrank.com/challenges/negative-lookahead/problem)

#### Task

You have a test string ***S***. 

Write a regex which can match all characters which are not immediately followed by that same character.

#### Solution

```python
Regex_Pattern = r"(.)(?!\1)"
```

