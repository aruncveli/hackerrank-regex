## [Matching Specific Characters](https://www.hackerrank.com/challenges/matching-specific-characters/problem)

#### Task

You have a test string ***S***.

Your task is to write a regex that will match ***S*** with following conditions: 

- Must be of length: **6**
- First character: **1**, **2** or **3**
- Second character: **1**, **2** or **0**
- Third character: **x**, **s** or **0**
- Fourth character: **3**, **0** , **A** or **a**
- Fifth character: **x**, **s** or **u**
- Sixth character: **.** or **,**

#### Solution

```python
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
```

