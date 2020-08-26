def modify_list(l):
    l[:] = [x // 2 for x in l if x%2 == 0]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(f"Before: {lst}")
    modify_list(lst)
    print(f"After: {lst}")