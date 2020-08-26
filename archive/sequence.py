n = int(input())
limit = n
for i in range(n):
    for k in range(i+1):
        print(i+1, end=' ')
        limit = limit - 1
        if limit <= 0:
            break
    if limit <= 0:
        break
