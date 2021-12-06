import math
from test import *
from p5 import *
res = 8
res_x = width / res
res_y = height / res

def setup():
        size(width, height)
        no_stroke()
        rect_mode("CENTER")


def draw():
        for i in range(20, width,  int(res_x)):
                for j in range(20, height, int(res_y)):
                        x = math.floor(i)
                        y = math.floor(j)
                        circle(x, y, 25)
        background(0)
if __name__ == '__main__':
        run()