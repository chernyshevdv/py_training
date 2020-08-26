import sys
from operator import add, sub, mul, floordiv


ops = {
        "plus": add,
        "minus": sub,
        "multiply": mul,
        "divide": floordiv
}

args = input().strip().lower().split()
if len(args) != 3:
    sys.exit(1)

val1, op, val2 = int(args[0]), args[1], int(args[2])
if op not in ops:
    sys.exit(1)

print(ops[op](val1, val2))
