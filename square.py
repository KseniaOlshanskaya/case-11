import turtle

def k(d, n):
    if n == 1:
        turtle.mainloop()
        return
    turtle.right(20)
    turtle.up()
    turtle.forward(d / 4)
    turtle.down()
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    return k(0.8 * d, n - 1)


def main():
    d = int(input('Длина стороны:'))
    n = int(input('Глубина рекурсии:'))
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    print(k(d * 0.8, n))


if __name__ == '__main__':
    main()
