#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def main():
    names = []  # 存储数据
    first_names = []
    rules = {}  # 从字表中找数据作为排序依据

    # 读入学生数据
    with open("class_sp_namelist.csv") as f1:
        for each_line in f1:
            result = re.search(r"^([0-9]{7})\t(.*?)\t(.*?)\t([\u2E80-\u9FFF])\t([\u2E80-\u9FFF]+)", each_line)
            temp = []
            for i in range(1, 6):
                temp.append(result[i])
            temp[1] += ' '
            names.append(temp)
            first_names.append(temp[1][0])
            first_names.append(temp[1][1])
            first_names.append(temp[1][2])

    # 读入字表，建立排序规则
    with open("汉字编码表 gbk unicode.txt") as f2:
        for each_line in f2:
            if each_line[0] in first_names:
                result = re.search(r"^[\u2E80-\u9FFF]\s{8}([a-z]+)\s+[a-z].{39}(.*?)\s", each_line)
                rules[each_line[0]] = [result[1], int(result[2])]
        rules[' '] = ['', 0]
    del first_names

    # 排序，按拼音排序只需要考虑前两个字；按笔画排序需要考虑全名的情况，因数据较少，故不存在三个字笔画均相同的学生，所以不需再去比较拼音
    names_sorted_by_pinyin = sorted(names, key=lambda x: (rules[x[1][0]][0], rules[x[1][1]][0]), )
    names_sorted_by_bihua = sorted(names, key=lambda x: (rules[x[1][0]][1], rules[x[1][1]][1], rules[x[1][1]][1]))

    print("按照拼音排序：\n序号    学号      姓名       拼音            性别   专业")
    flag = 1
    for i in names_sorted_by_pinyin:
        print("{:>2d}    {}    {:　<6s}{:<16s}{:<5s}{}".format(flag, i[0], i[1], i[2], i[3], i[4]))
        flag += 1

    print("\n按照笔画排序：\n序号  笔画1 笔画2 笔画3    学号      姓名       拼音            性别   专业")
    flag = 1
    for i in names_sorted_by_bihua:
        print("{:>2d}    {:>2d}    {:>2d}    {:>2d}    {}    {:　<6s}{:<16s}{:<5s}{}".format(flag,
                                                                                            rules[i[1][0]][1],
                                                                                            rules[i[1][1]][1],
                                                                                            rules[i[1][2]][1],
                                                                                            i[0], i[1], i[2], i[3], i[4]
                                                                                            ))
        flag += 1


if __name__ == '__main__':
    main()
