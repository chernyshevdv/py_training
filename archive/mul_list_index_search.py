numbers = [int(i) for i in input().strip().split()]
subject = int(input().strip())
sublist = [index for index, value in enumerate(numbers) if value == subject]
print(*(sublist or ['None']))