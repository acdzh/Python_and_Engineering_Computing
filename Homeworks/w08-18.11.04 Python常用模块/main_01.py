import random
from time import time


# H，锤 S, 剪刀，  c 布


def WhoWin(hsc_tom, hsc_jerry):
    results = (('H', 'S', 'T'),
               ('H', 'C', 'J'),
               ('S', 'H', 'J'),
               ('S', 'C', 'T'),
               ('C', 'H', 'T'),
               ('C', 'S', 'J')
               )
    if hsc_tom == hsc_jerry:
        return 'D'  # draw
    else:
        for i in results:
            if hsc_tom == i[0] and hsc_jerry == i[1]:
                return i[2]


def main():
    moves = ['H', 'S', 'C']
    random.seed(time())
    tom_move = random.choice(moves)
    jerry_move = random.choice(moves)
    result = WhoWin(tom_move, jerry_move)
    print('Tom: %s, Jerry: %s, Result: %s' % (tom_move, jerry_move, result))


if __name__ == '__main__':
    main()
