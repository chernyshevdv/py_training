import collections

num_list = [int(x) for x in input().split()]
counter = collections.Counter(num_list)
values = [value for (value, count) in counter.items() if count > 1]
print(*values)
