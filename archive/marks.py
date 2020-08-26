stats = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
marks = input().strip().split()

for mark in marks:
    stats[mark] += 1

print("{:.2f}".format(stats['A'] / sum(stats.values())))