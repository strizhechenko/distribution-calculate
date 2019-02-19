# distribution-calculate
What if I add random sleep in range from X to Y, how may it distribute Z events in this interval?

## example

Given:

- 600 events per second.
- we want to add sleep $((RANDOM % 30))

``` shell
python3 main.py --min 0 --max 30 --events 600
0: 15
1: 25
2: 31
3: 20
4: 14
5: 14
6: 18
7: 21
8: 18
9: 19
10: 25
11: 13
12: 17
13: 20
14: 23
15: 20
16: 12
17: 26
18: 19
19: 17
20: 17
21: 17
22: 16
23: 27
24: 19
25: 28
26: 23
27: 23
28: 27
29: 16
min: 12
avg: 20
max: 31
```
