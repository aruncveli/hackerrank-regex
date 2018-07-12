## [Detect the Email Addresses](https://www.hackerrank.com/challenges/detect-the-email-addresses/problem)

#### Task

You will be provided with a block of text, spanning not more than hundred lines. Your task is to find the unique e-mail addresses present in the text.

#### Solution Pattern

```python
regex = r'\b(?:\w|\.)+@(?:\w*\.*)+\b'
```

