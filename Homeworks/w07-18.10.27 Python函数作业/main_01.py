# -*- coding: utf-8 -*-
"""
这里给的条件互相之间有重叠，不太清楚怎么办
像输入istriangle(1,5,3,-2)的话，不清楚是该输出不能构成三角形还是有参数小于零
默认直接按照后者处理
"""


def istriangle(*param):
    """
    this function is to determine whether a triangle can be formed.
    :param param: three integer, and the Letters will be filtered.
    :return:nothing
    """

    param = list(filter(lambda x: type(x) in [int, float], param))
    if len(param) < 3:
        s = '参数不够'
    else:
        for i in param:
            if i <= 0:
                s = '有参数小于0'
            else:
                if param[0] + param[1] > param[2] and param[1] + param[2] > param[0] and param[0] + param[2] > param[1]:
                    s = '可以构成三角形'
                else:
                    s = '不可以构成三角形'
    print(s)


def main():
    istriangle(3, 2, 3)  # 输出“可以构成三角形”
    istriangle(3, 1, 1)  # 输出“不可以构成三角形”
    istriangle(3, 2, 'a', -1)  # 输出"有参数小于0！"
    istriangle(3, 2, 'a', 3)  # 取参数中前面3个有效数来判断是否能够成三角形，输出“可以构成三角形”
    istriangle(3, 2)  # 输出“参数不够”

if __name__ == '__main__':
    main()
