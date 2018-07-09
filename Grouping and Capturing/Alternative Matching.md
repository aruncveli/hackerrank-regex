## [Alternative Matching](https://www.hackerrank.com/challenges/alternative-matching/problem)

#### Task

Given a test string ***S***, write a RegEx that matches ***S*** under the following conditions:  

-  must start with ***Mr., Mrs., Ms., Dr.*** or ***Er.***.  
- The rest of the string must contain only ***one or more*** English alphabetic letters (upper and lowercase).

#### Solution

```python
Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er).[a-zA-Z]+$'
```

