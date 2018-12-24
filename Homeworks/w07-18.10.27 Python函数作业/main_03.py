# -*- coding: utf-8 -*-
import random
from math import sqrt

import numpy as np
import cv2


def distance(x1, y1, x2, y2):
    delta_x = x1 - x2
    delta_y = y1 - y2
    return sqrt(delta_x * delta_x + delta_y * delta_y)


def generate2circles(lim_A_x=0, lim_A_y=0, lim_B_x=10, lim_B_y=10) -> dict:
    """  本函数在两个点A、B所围成的矩形中，生成2个大小位置都随机的圆形
         要求返回一个具有一个元素元组。
         同时特别注意：两个圆不能超出这个矩形，同时两个圆不能有交集
         输入参数：
         lim_A_x : A点的x坐标
         lim_A_y : A点的y坐标
         lim_B_x : B点的x坐标
         lim_B_y : B点的y坐标
         输出参数：
         c1x : 1#圆心x坐标
         c1y : 1#圆心y坐标
         c1r : 1#圆半径r
         c2x : 2#圆心x坐标
         c2y : 2#圆心y坐标
         c2r : 2#圆半径r
    """
    c1x = random.uniform(lim_A_x, lim_B_x)
    c1y = random.uniform(lim_A_y, lim_B_y)
    c2x = random.uniform(lim_A_x, lim_B_x)
    c2y = random.uniform(lim_A_y, lim_B_y)
    c1r = random.uniform(0, min(abs(c1x - lim_A_x), abs(c1x - lim_B_x), abs(c1y - lim_A_y), abs(c1y - lim_B_y),
                                distance(c1x, c1y, c2x, c2y)))
    c2r = random.uniform(0, min(abs(c2x - lim_A_x), abs(c2x - lim_B_x), abs(c2y - lim_A_y), abs(c2y - lim_B_y),
                                abs(distance(c1x, c1y, c2x, c2y) - c1r)))
    return (c1x, c1y, c1r, c2x, c2y, c2r)


def draw(rantangle, circle):
    """测试函数(用opencv画图)"""
    times = 1200 // abs(rantangle[2] - rantangle[0])
    for i in range(0, len(rantangle)):
        rantangle[i] = int(times * rantangle[i])
    for i in range(0, len(circle)):
        circle[i] = abs(int(times * circle[i]))

    print(rantangle)
    print(circle)
    img = np.zeros((abs(rantangle[1] - rantangle[3]), abs(rantangle[0] - rantangle[2]), 3), dtype="float64")
    cv2.circle(img, (circle[0], abs(abs(rantangle[1] - rantangle[3]) - circle[1])), circle[2], (0, 0, 255), -1, 8)
    cv2.circle(img, (circle[3], abs(abs(rantangle[1] - rantangle[3]) - circle[4])), circle[5], (0, 255, 0), -1, 8)
    cv2.imshow('test', img)
    cv2.waitKey(0)


def main():
    circles = generate2circles(0, 0, 100, 50)
    print(circles)
    draw([0, 0, 100, 50], list(circles))


if __name__ == '__main__':
    while True:
        main()
