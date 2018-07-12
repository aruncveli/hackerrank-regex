## [Detect HTML Tags](https://www.hackerrank.com/challenges/detect-html-tags/problem)

#### Task

To detect the various *tags* used in an HTML document, self-closing tags included.

#### Solution Pattern

```python
Regex_Pattern = r'(?<=<)\w+'
```

