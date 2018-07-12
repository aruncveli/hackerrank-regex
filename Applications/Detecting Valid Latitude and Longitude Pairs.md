## [Detecting Valid Latitude and Longitude Pairs](https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem)

#### Task

Given a line of text which possibly contains the latitude and longitude  of a point, can you use regular expressions to identify the latitude and longitude referred to (if any)?

For (X, Y), -90<=X<=+90 and -180<=Y<=180

#### Solution Pattern

```python
regex = r'^\(' + \
        '[-+]?(([1-8]?[0-9]|0)(\.\d+)?|90(\.0+)?),' + '\s' + \
        '[-+]?((1?[1-7]?[0-9]|10[0-9]|[1-9][0-9]|0)(\.\d+)?|180(\.0+)?)' + \
        '\)$'
```

