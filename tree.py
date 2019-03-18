import turtle


def o(h, n, a):
    if n == 0:
        return
    turtle.forward(h)
    turtle.right(a)
    o(h * 0.5, n - 1, a)
    turtle.left(2*a)
    o(h * 0.5, n - 1, a)
    turtle.right(a)
    turtle.backward(h)


def main():
    h = int(input("Введите длину ветки: "))
    a = int(input("Введите угол наклона: "))
    n = int(input("Введите глубину рекурсии: "))
    turtle.left(90)
    print(o(h, n-1, a))
    turtle.mainloop()

if __name__ == "__main__":
    main()