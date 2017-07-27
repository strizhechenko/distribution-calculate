# distribution-calculate
What if I add random sleep in range from X to Y, how may it distribute Z events in this interval?

## example

Given:

- 600 events per second.
- we want to add sleep $((RANDOM % 30))

``` shell
python3 main.py --min 0 --max 30 --events 600
0: 14
1: 15
2: 18
3: 13
4: 18
5: 17
6: 17
7: 25
8: 25
9: 18
10: 19
11: 20
12: 17
13: 26
14: 23
15: 15
16: 18
17: 17
18: 16
19: 20
20: 17
21: 20
22: 26
23: 24
24: 15
25: 26
26: 20
27: 23
28: 19
29: 19
30: 20
min: 13
max: 26
```
