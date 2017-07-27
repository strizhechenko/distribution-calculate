#!/usr/bin/env python3

from random import randint
from collections import Counter
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--min', type=int, default=0)
parser.add_argument('--max', type=int)
parser.add_argument('--events', type=int)
options = parser.parse_args()

times = [randint(options.min, options.max) for _ in range(options.events)]
distribution = Counter(times)

for k, v in sorted(distribution.items()):
    print("{0}: {1}".format(k, v))

print("min:", min(dict(distribution).values()))
print("max:", max(dict(distribution).values()))
