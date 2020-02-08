import turtle
print('''Select a fractal:
1. The Koch Curve
2. Koch's Snowflake.
3. Ice fractal (example 1)
4. Ice fractal (example 2)
5. Snowflake to an ice fractal (example 1) with the construction of external and internal fractals.
6. A snowflake to an ice fractal (example 2) with the construction of the outer and inner fractals.
7. Minkowski Curve
8. Levi's Curve
9. Building a binary tree.''')

def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)

def main():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
n = int(input('Глубина рекурсии:'))
a = int(input('Длина стороны:'))
koch(n, a)

main()