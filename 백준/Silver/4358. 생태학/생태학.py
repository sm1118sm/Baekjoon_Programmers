import sys
from collections import defaultdict

tree_counter = defaultdict(int)
total = 0

for line in sys.stdin:
    name = line.strip()
    if name:
        tree_counter[name] += 1
        total += 1

for name in sorted(tree_counter):
    percentage = (tree_counter[name] / total) * 100
    print(f"{name} {percentage:.4f}")