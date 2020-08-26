sequence = list(map(int, input().strip().split()))
n = len(sequence)
if n == 1:
    print("Jolly")
    exit()

jolly_set = set(range(1, n))
sample_set = set()
for i in range(len(sequence)-1):
    sample_set.add(abs(sequence[i]-sequence[i+1]))

if sample_set.symmetric_difference(jolly_set) == set():
    print("Jolly")
else:
    print("Not jolly")
