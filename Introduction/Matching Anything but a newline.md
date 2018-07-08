## [Matching Anything But a Newline](https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem)

#### Task

You have a test string ***S***. 

Your task is to write a regular expression that matches only and exactly strings of form: ***abc.def.ghi.jkx***, where each variable ***a, b, c, d, e, f, g, h, i, j, k*** and ***x*** can be any single character except the newline.

#### Solution

`regex_pattern = r"^...\....\....\....$"`