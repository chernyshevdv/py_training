import collections

source = input().strip().lower().split()
freq = collections.Counter(source)
for word, val in freq.items():
    print(f"{word} {val}")
