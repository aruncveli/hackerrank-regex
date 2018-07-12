## [Build a Stack Exchange Scraper](https://www.hackerrank.com/challenges/stack-exchange-scraper/problem)

#### Task

You will be provided with the markup of question listing pages from Stack Exchange, from which you need to detect: 

1. Identifier 
2. Question text (which is on the Hyperlink to the question)
3. How long ago the question was asked

#### Solution Pattern

```python
regex = r'question-summary-(\w\w\w\w\w)".*?class="question-hyperlink">(.+?)</a>.*?class=\"relativetime\">(.+?)</span>'
```
