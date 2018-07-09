## [Forward References](https://www.hackerrank.com/challenges/forward-references/problem)

Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, PHP, Delphi and Ruby regex flavors. The solution provided is written in Java.

#### Task

You have a test string ***S***. 

Your task is to write a regex which will match ***S***, with following conditions:

- ***S*** consists of **tic** or **tac**.  
- **tic** should not be an immediate neighbour of itself.  
- The first **tic** must occur only when **tac** has appeared at least twice before.

#### Solution

```java
tester.checker("^tac(tac(tic)?)*$");
```

