# Memoized Solution to Change-Making Problem

This is a solution to the change-making problem, which entails making an exact amount of change with the fewest possible number of coins given a total amount and the value of each coin. It also uses memoization for efficiency. It is guaranteed to find the optimal solution and has complexity O(nk).

In order to run this program, issue the following commands.

```
g++ dynamicChange.cpp -o dc
./dc [space-separated arguments here]
```

Your arguments should be in the following format, where ```n``` is the number of cents to make change for, ```k``` is the number of distinct coin types, and ```d1``` through ```dk``` are the number of cents represented by each coin type (in any order):

```
n k d1 d2 ... dk
```

For example, to find the solution for making 78 cents using the US coin system, the command would be:

```
./dc 78 4 1 5 10 25
```

The output of dynamicChange.cpp is in the format:

```
coins used: [value of each coin used]
[time elapsed in microseconds] microseconds elapsed
```