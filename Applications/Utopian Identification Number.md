## [Utopian Identification Number](https://www.hackerrank.com/challenges/utopian-identification-number/problem)

#### Task

A new identification number is given for every Citizen of the Country Utopia and it has the following format.

- The string must begin with between 0-3 (inclusive) lowercase letters.
- Immediately following the letters, there must be a sequence of digits (0-9). The length of this segment must be between 2 and 8, both  inclusive.  
- Immediately following the numbers, there must be atleast 3 uppercase letters. 

Your task is to find out if a given identification number is valid or not.

#### Solution Pattern

```python
regex = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'
```

