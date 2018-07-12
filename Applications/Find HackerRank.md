## [Find HackerRank](https://www.hackerrank.com/challenges/find-hackerrank/problem)

#### Task

At HackerRank, we always want to find out how popular we are getting  every day and have scraped conversations from popular sites. Each  conversation  fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says *hackerrank* (all in lowercase). We would like you to help us figure out whether a conversation:

1. Starts with *hackerrank*
2. Ends with *hackerrank*
3. Start and ends with *hackerrank*

#### Solution Pattern

```python
start = r'^hackerrank'
end = r'hackerrank$'
start_end = r'^(hackerrank|(hackerrank.*?hackerrank))$'
```

