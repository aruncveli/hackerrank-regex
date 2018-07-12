## [Alien Username](https://www.hackerrank.com/challenges/alien-username/problem)

#### Task

Match alien usernames with the following format:

1. It *must* begin with either an underscore, `_` (ASCII value ), or a period, `.` (ASCII value ).
2. The first character *must* be immediately followed by *one or more* digits in the range 0 through 9.
3. After some number of digits, there *must* be  or more English letters (uppercase and/or lowercase).
4. It *may* be terminated with an optional `_` (ASCII value ). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.

Given *n* strings, determine which ones are valid alien usernames. If a string is a valid alien username, print `VALID` on a new line; otherwise, print `INVALID`.

#### Solution Pattern

```python
Regex_Pattern = r'^[_\.]\d+[a-zA-Z]*_?$'
```

