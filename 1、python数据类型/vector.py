# #!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 15:05
# @Author : v_ruivzhou
from math import hypot

"""定义向量类模拟数值类型"""


class Vector:
    """实现一个二维向量（vector）类"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector:[{},{}]'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.y
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
