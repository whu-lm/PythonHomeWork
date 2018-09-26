"""
作者：18级嵌入式1班刘茂，学号：SA18225243
时间：2018-09-20

Programming Work1
根据半径，求球体的表面积和体积
"""
from math import pi,pow

def V(r):
    v = 4/3*pi*pow(r,3)
    return float('{:.2f}'.format(v))
def S(r):
    s = 4*pi*pow(r,2)
    return float('{:.2f}'.format(s))
def demo():
    print("{0:*^40}".format("Programming Work1"))
    print("根据输入的球体半径，求球体的表面积和体积")
    print("输入D,程序退出！")
    print("{0: ^40}".format("By:liumao,SA18225243"))
    print("{0: ^40}".format("Date:2018-09-20"))
    print("*"*40)

    while 1:
        r = input("请输入球体的半径：")
        if(r == 'D'):
            print("程序退出")
            break
        try:
            f_r = float(r)
        except (TypeError,ValueError):
            print("你的输入不合法，请重新输入：")
            continue
        print("体积是：",V(f_r))
        print("表面积是：",S(f_r))
demo()