## [Branch Reset Groups](https://www.hackerrank.com/challenges/branch-reset-groups/problem)

Branch reset group is supported by Perl, PHP, Delphi and R. The solution provided is written in Perl.

#### Task

You have a test string ***S***. 

Your task is to write a regex which will match ***S***, with following conditions:

- ***S*** consists of 8 digits. 
- ***S*** must have "**---**", "**-**", "**.**" or "**:**" separator such that string ***S*** gets divided into ***4*** parts, with each part having exactly two digits.  
- ***S*** must have exactly one kind of separator.  
- Separators must have integers on both sides.

#### Solution

```perl
$Regex_Pattern = '^\d\d(?|(-)|(---)|(.)|(:))\d\d\1\d\d\1\d\d$';
```

