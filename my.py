from turtle import *

def koch(order, size):

    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

def main():
    up()
    goto(-100,0)
    down()
n = 3
a = 500
koch(n,a)
right(60)
koch(n,a)
right(60)
koch(n,a)

main()