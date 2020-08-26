import re

TOKENS = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
          'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
          }


def convert_pop(text):
    PREFIXES = {'I': ('V', 'X'), 'X': ('L', 'C'), 'C': ('D', 'M')}

    instr = list(text)
    lexemas = []
    while len(instr) > 0:
        token = instr.pop(0)
        if token in PREFIXES.keys() and instr[0] in PREFIXES[token]:
            token += instr.pop(0)
        lexemas.append(token)

    return sum([TOKENS[l] for l in lexemas])


def convert_re(text):
    pattern = "|".join(TOKENS.keys())
    lexemas = re.findall(pattern, text)
    return sum([TOKENS[lex] for lex in lexemas])


print(convert_re(input().strip()))
