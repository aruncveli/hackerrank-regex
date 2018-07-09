## [Matching Start & End](https://www.hackerrank.com/challenges/matching-start-end/problem)

#### Task

You have a test string ***S***. Your task is to match the pattern ***Xxxxx.*** . 

Here, ***x*** denotes a word character, and ***X*** denotes a digit. 

***S*** must start with a digit and end with `.` symbol. 

***S*** should be ***6*** characters long only.

#### Solution

```python
Regex_Pattern = r"^\d\w\w\w\w.$"
```
