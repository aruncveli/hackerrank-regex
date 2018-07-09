## [Matching Word & Non-Word Character](https://www.hackerrank.com/challenges/matching-word-non-word/problem)

#### Task

You have a test string ***S***. 

Your task is to match the pattern ***xxxXxxxxxxxxxxXxxx***. 

Here ***x*** denotes any word character and ***X*** denotes any non-word character.

#### Solution

```python
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"
```