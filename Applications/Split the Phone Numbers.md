## [Split the Phone Numbers](https://www.hackerrank.com/challenges/split-number/problem)

#### Task

There is a list of phone numbers which needs the attention of a text  processing expert. As an expert in regular expressions, you are being  roped in for the task. A phone number directory can reveal a lot such as country codes and  local area codes. The only constraint is that one should know how to  process it correctly.  

A Phone number is of the following format:

```python
[Country code]-[Local Area Code]-[Number]
```



There might either be a '-' ( ascii value 45), or a ' '( space, ascii value 32) between the segments 

 Where the country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each.

#### Solution Pattern

```python
regex = r'(^\d{1,3}[- ]\d{1,3}[- ]\d{4,10})$'
```

