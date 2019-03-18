import turtle


def ice(a, n):
    if n == 0:
        turtle.forward(a)
        return
    ice(a, n - 1)
    turtle.left(90)
    ice(a / 2, n - 1)
    turtle.right(180)
    ice(a / 2, n - 1)
    turtle.left(90)
    ice(a, n - 1)


def main():
    a = int(input("Введите длину: "))
    n = int(input("Введите глубину рекурсии: "))
    turtle.up()
    turtle.backward(500)
    turtle.down()
    ice(a, n)
    turtle.mainloop()


if __name__ == "__main__":
    main()