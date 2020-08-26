# LCD segments
sx__x = ' -- '
s1xx1 = '|  |'
sxxxx = '    '
sxxx1 = '   |'
s1xxx = '|   '

# LCD digits
digits = {
    '0': [sx__x, s1xx1, s1xx1, sxxxx, s1xx1, s1xx1, sx__x],
    '1': [sxxxx, sxxx1, sxxx1, sxxxx, sxxx1, sxxx1, sxxxx],
    '2': [sx__x, sxxx1, sxxx1, sx__x, s1xxx, s1xxx, sx__x],
    '3': [sx__x, sxxx1, sxxx1, sx__x, sxxx1, sxxx1, sx__x],
    '4': [sxxxx, s1xx1, s1xx1, sx__x, sxxx1, sxxx1, sxxxx],
    '5': [sx__x, s1xxx, s1xxx, sx__x, sxxx1, sxxx1, sx__x],
    '6': [sx__x, s1xxx, s1xxx, sx__x, s1xx1, s1xx1, sx__x],
    '7': [sx__x, sxxx1, sxxx1, sxxxx, sxxx1, sxxx1, sxxxx],
    '8': [sx__x, s1xx1, s1xx1, sx__x, s1xx1, s1xx1, sx__x],
    '9': [sx__x, s1xx1, s1xx1, sx__x, sxxx1, sxxx1, sx__x]
}


def print_bar(text):
    print("x" + '-' * (5 * len(text) - 1) + "x")


def print_text(text):
    print_bar(text)
    for row in range(7):
        print("|", end='')
        row_seg = []
        for char in text:
            row_seg.append(digits[char][row])
        print(*row_seg, sep=' ', end="|\n")
    print_bar(text)


if __name__=='__main__':
    text = input("Enter formula (e.g. 3+5): ").strip()
    print_text(str(eval(text)))