import turtle

def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order - 1, size / 3)
        turtle.left(60)
        koch(order - 1, size / 3)
        turtle.right(120)
        koch(order - 1, size / 3)
        turtle.left(60)
        koch(order - 1, size / 3)


def sne(order, size):
    for i in range(3):
        if i == 0:
            koch(order, size)
        else:
            turtle.right(120)
            koch(order, size)



def main():
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    turtle.speed(0)
    sne(n, a)
    turtle.mainloop()


if __name__ == "__main__":
    main()
