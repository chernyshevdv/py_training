import re


pattern = r"(\d*)(\D)"
decoded = ""
for num, char in re.findall(pattern, input().strip()):
    num = int(num) if num else 1
    decoded += char * num

print(decoded)
