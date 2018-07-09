## [Matching {x, y} Repetitions](https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem)

#### Task

You have a test string ***S***.

Your task is to write a regex that will match ***S*** using the following conditions: 

- Should begin with 1 or 2 **digits**.
- After that, ***S*** should have 3 or more **letters** (both lowercase and uppercase). 
- Then ***S*** should end with up to 3 **.** symbol(s). You can end with 0 to 3 `.` symbol(s), inclusively.

#### Solution

```python
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'
```

