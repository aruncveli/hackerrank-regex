## [Matching {x} Repetitions](https://www.hackerrank.com/challenges/matching-x-repetitions/problem)

#### Task

You have a test string ***S***.

Your task is to write a regex that will match ***S*** using the following conditions: 

- Must be of length equal to **45**.
- The first ***40*** characters should consist of **letters** (both lowercase and uppercase) or of **even digits**.  
- The last ***5*** characters should consist of **odd digits** or **whitespace characters**.

#### Solution

```python
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
```

