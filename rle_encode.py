import re
pattern = r"((\w)\2*)"
for sequence, char in re.findall(pattern, input()):
    repeats = str(len(sequence)) if sequence != char else ""
    print(repeats + char, end='')
