## [Detect the Domain Name](https://www.hackerrank.com/challenges/detect-the-domain-name/problem)

#### Task

You will be provided with a chunk of HTML markup. Your task is to identify the unique domain names from the links or Urls which are present in the markup fragment.

#### Solution Pattern

```python
regex = r'https?://(?:ww[w2]\.)?([a-zA-Z\d-]+(?:\.[a-zA-Z\d-]+)+)'
```

