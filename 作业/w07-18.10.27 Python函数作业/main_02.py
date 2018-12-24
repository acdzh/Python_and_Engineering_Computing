# -*- coding: utf-8 -*-
def get_max(lst):
    lst = list(filter(lambda x: type(x) in [int, float], lst))
    if len(lst) == 0:
        return 0
    else:
        my_max = lst[0]
        for each in lst:
            if each > my_max:
                my_max = each
    return my_max

def main():
    list1 = ['b', 'c', 23, -59, 32, 'a', 76, 20]
    print(get_max(list1))


if __name__ == '__main__':
    main()