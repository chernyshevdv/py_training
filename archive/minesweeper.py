from collections import Counter


height, width = [int(arg) for arg in input().strip().split()]

field = []
# field is a list of strings
for i in range(height):
    field.append(input().strip())

guess = []
# guess is a list of lists
for row in range(height):
    guess.append(list("o" * width))  # initialize guess with o symbols
    for col in range(width):
        if field[row][col] == '*':
            guess[row][col] = '*'
            continue
        mines = 0
        # calculate top-left and bottom-right corners of 3x3 window around current position
        top = row - 1 if row - 1 > 0 else 0
        bottom = row + 1 if row + 1 < height else height - 1
        left = col - 1 if col - 1 > 0 else 0
        right = col + 1 if col + 1 < width else width - 1
        # compose a buffer of all symbols in the window
        buffer = ""
        for y in range(top, bottom+1):
            buffer += field[y][left:right+1]
        mines = Counter(buffer)['*']  # count all * in the buffer
        guess[row][col] = str(mines)

for row in guess:
    print("".join(row))
