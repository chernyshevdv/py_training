import re


def replace_re():
    pattern = r" +"
    instr = input().strip()
    print(re.sub(pattern, "_", instr))


def split_and_join():
    print(
        "_".join(
            input().strip().split()
        )
    )


split_and_join()  # this one is better
# replace_re() is also good
