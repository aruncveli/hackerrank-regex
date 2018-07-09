## [Negative Lookbehind](https://www.hackerrank.com/challenges/negative-lookbehind/problem)

#### Task

You have a test String ***S***. 

Write a regex which can match all the occurences of characters which are ***not*** immediately preceded by ***vowels*** (a, e, i, u, o, A, E, I, O or U).

#### Solution

```python
Regex_Pattern = r"(?<![aeiouAEIOU])."
```

