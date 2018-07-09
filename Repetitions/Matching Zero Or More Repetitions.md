## [Matching Zero Or More Repetitions](https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions/problem)

#### Task

You have a test string ***S***.

Your task is to write a regex that will match ***S*** using the following conditions: 

-  Should begin with 2 or more **digits**.
-  After that, ***S*** should have 0 or more **lowercase letters**. 
-  Should end with 0 or more **uppercase letters**.

#### Solution

```python
Regex_Pattern = r'^\d{2,}[a-z][A-Z]$'
```

