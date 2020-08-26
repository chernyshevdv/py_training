import re


def replace_with_re():
    pattern = r"(\b\w|\_\w)"
    inp = input().strip()
    out = re.sub(pattern, lambda x: x.group()[-1].upper(), inp)
    print(out)


def replace_with_title():
    print(
        input().strip().title().replace('_', '')
    )


def replace_with_join():
    inp = input().strip().split('_')
    arr_out = [x.capitalize() for x in inp]
    print("".join(arr_out))


replace_with_join()
