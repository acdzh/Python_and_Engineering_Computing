import random


def shuffle(list):
    for i in range(len(list) - 1, 0, -1):
        temp = random.randrange(0, i + 1)
        list[i], list[temp] = list[temp], list[i]
    return list

def translate(list):
    colors = "♠♥♣♦"
    s = ''
    for i in list:
        if i == 52:
            s += "♛\t\t"
        elif i == 53:
            s += "♚\t\t"
        else:
            number = i // 4 + 1
            c_color = colors[i % 4]
            if number == 1:
                s += ('A' + c_color + '\t\t')
            elif number == 11:
                s += ('J' + c_color + '\t\t')
            elif number == 12:
                s += ('Q' + c_color + '\t\t')
            elif number == 13:
                s += ('K' + c_color + '\t\t')
            else:
                s +=(str(number) + c_color + '\t\t')
    return s

def find_bomb(list):
    bomb = [[], [], []]
    for player in range(0,3):
        for i in range(0, 17):
            list[player][i] = list[player][i] // 4 + 1
        for i in range(0, min(14, max(list[player]) + 1)):
            if list[player].count(i) == 4:
                if i == 1:
                    bomb[player].append('A')
                elif i == 11:
                    bomb[player].append('J')
                elif i == 12:
                    bomb[player].append('Q')
                elif i == 13:
                    bomb[player].append('K')
                else:
                    bomb[player].append(str(i))
        if list[player].count(14) == 2:
            bomb[player].append('王炸')
        if bomb[player]:
            s = '玩家' + str(player + 1) + '有炸弹:'
            for i in bomb[player]:
                s += (' ' + i)
            s += ';'
            print(s)
    if not (bomb[0] or bomb[1] or bomb[2]):
        print('三个玩家均无炸弹')






    return bomb


card0 = shuffle(list(range(0,54)))
cards =[]
for i in range(0, 51, 17):
    cards.append(sorted(card0[i : i + 17]))
cards.append(sorted(card0[-3 : ]))

for i in range(0, 4):
    s = "3张底牌为：\t" + translate(cards[i]) if i == 3 else "玩家" + str(i + 1) + "的牌为：\t" + translate(cards[i])
    print(s)

print('\n')
find_bomb(cards)



























