## [Detect HTML links](https://www.hackerrank.com/challenges/detect-html-links/problem)

#### Task

To strip the *links*  and the *text name* from the html pages.

#### Solution Pattern

```python
link_and_text = r'<a href=\"(.*?)\".*?>([\w ,./]*)(?=</)'
```