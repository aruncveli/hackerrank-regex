## [Saying Hi](https://www.hackerrank.com/challenges/saying-hi/problem)

#### Task

Given a sentence, write a RegEx to match the following criteria:   

1. The first character must be the letter ***H*** or ***h***.
2. The second character must be the letter ***I*** or ***i*** .
3. The third character must be a single space (i.e.: ***\s***). 
4. The fourth character *must not* be the letter ***D*** or ***d***.

Given ***n*** lines of sentences as input, print each sentence matching your RegEx on a new line.

#### Solution Pattern

```python
regex = r'^[hH][iI]\s[^dD]'
```

