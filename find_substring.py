import re

source = input().strip()
pattern = f"(?={input().strip()})"
print(
    *[match.start() for match in re.finditer(pattern, source)] or ['-1']
)