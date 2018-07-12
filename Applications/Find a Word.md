## [Find a Word](https://www.hackerrank.com/challenges/find-a-word/problem)

#### Task

We define a word as a non-empty maximum sequence of characters that  can contain only lowercase letters, uppercase letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word  has to be immediately preceeded by a character not allowed to occur in a  word or by the left boundary of the sentence, and it has to be  immediately followed by a character not allowed to occur in a word or by  the right boundary of the sentence.

Given *N* sentences and *T* words, for each of these words, find the number of its occurences in all the *N* sentences.

#### Solution Pattern

```python
regex = r'\b' + word + r'\b'
```

