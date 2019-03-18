import turtle


def levi(a, n):
    if n == 0:
        turtle.forward(a)
        return
    turtle.left(45)
    levi(a/2, n - 1)
    turtle.right(90)
    levi(a/2, n - 1)
    turtle.left(45)


def main():
    a = int(input("Введите длину: "))
    n = int(input("Введите глубину рекурсии: "))
    turtle.up()
    turtle.backward(500)
    turtle.down()
    levi(a, n)
    turtle.mainloop()


if __name__ == "__main__":
    main()