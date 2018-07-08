## [Matching One Or More Repetitions](https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem)

#### Task

You have a test string ***S***. 
 Your task is to write a regex that will match ***S*** using the following conditions:  

-  should begin with 1 or more **digits**.
- After that,  should have 1 or more **uppercase letters**. 
-  should end with 1 or more **lowercase letters**.

#### Solution

`Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'`