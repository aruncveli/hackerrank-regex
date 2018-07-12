## [UK and US: Part 2](https://www.hackerrank.com/challenges/uk-and-us-2/problem)

#### Task

We've already seen how UK and US words [differ](https://www.hackerrank.com/challenges/uk-and-us) in their spelling. One other difference is how UK has kept the usage of letters *our* in some of its words and US has done away with the letter *u* and uses just *or*. Given the UK format of the word that has *our* in it, find out the total number of occurrences of both its UK and US variants in a given sequence of words.

#### Solution Pattern

```python
uk_us_spelling = re.sub('our', 'ou?r', uk_spelling)
regex = r'\b' + uk_us_spelling + r'\b'
```

