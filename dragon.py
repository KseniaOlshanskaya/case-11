import turtle


def love(d, n):
    if n == 0:
        return
    love(d, n - 1)
    turtle.right(90)
    hate(d, n - 1)
    turtle.forward(d)
    turtle.right(90)


def hate(d, n):
    if n == 0:
        return
    turtle.left(90)
    turtle.forward(d)
    love(d, n - 1)
    turtle.left(90)
    hate(d, n - 1)


def main():
    d = int(input('Длина стороны:'))
    n = int(input('Глубина рекурсии:'))
    turtle.left(90)
    turtle.forward(d)
    love(d, n - 1)
    turtle.mainloop()


if __name__ == "__main__":
    main()
