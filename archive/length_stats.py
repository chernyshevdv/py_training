from collections import Counter

lens = [len(word) for word in input().lower().split(' ')]
counter = Counter(lens)
for ln in sorted(counter.keys()):
    print(f"{ln}: {counter[ln]}")
