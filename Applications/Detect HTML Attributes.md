## [Detect HTML Attributes](https://www.hackerrank.com/challenges/html-attributes/problem)

#### Task

To create a list of all the attributes of every tag found in the given HTML page.

#### Solution Pattern

```python
tag_regex = r'<(\w+)(|\s+[^>]*)>' # To be applied to the given input HTML
attribute_regex = r'\w+(?==[\'\"])' # To be applied to the detected tags
```