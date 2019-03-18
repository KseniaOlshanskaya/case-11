import turtle


def ice2(a, n):
    if n == 0:
        turtle.forward(a)
        return
    ice2(a, n - 1)
    turtle.left(135)
    ice2(a/2, n - 1)
    turtle.right(180)
    ice2(a/2, n - 1)
    turtle.left(90)
    ice2(a / 2, n - 1)
    turtle.right(180)
    ice2(a / 2, n - 1)
    turtle.left(135)
    ice2(a, n - 1)


def main():
    a = int(input('Введите длину: '))
    n = int(input('Ведите глубину рекурсии: '))
    turtle.up()
    turtle.backward(500)
    turtle.down()
    ice2(a, n)
    turtle.mainloop()


if __name__ == "__main__":
    main()