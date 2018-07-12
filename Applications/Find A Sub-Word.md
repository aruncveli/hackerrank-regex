## [Find A Sub-Word](https://www.hackerrank.com/challenges/find-substring/problem)

#### Task

We define a *word* to be a contiguous sequence of one or more word characters that is preceded and succeeded by one or more occurrences of non-word-characters or line terminators.

We define a *sub-word* as follows:

- A sequence of word characters (i.e., English alphabetic letters,  digits, and/or underscores) that occur in the same exact order (i.e., as  a contiguous sequence) inside another word.
- It is preceded and succeeded by word characters *only*.

Count the number of occurences of a given *sub-word* in all the given *words*.

#### Solution Pattern

```python
Regex_Pattern = r'\B' + subword + '\B'
```