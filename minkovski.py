import turtle

def rin(d, n):
    if n == 0:
        turtle.forward(d)
        return
    while n != 0:
        n -= 1
        d //= 4
        rin(d, n)
        turtle.left(90)
        rin(d, n)
        turtle.right(90)
        rin(d, n)
        turtle.right(90)
        rin(d, n)
        rin(d, n)
        turtle.left(90)
        rin(d, n)
        turtle.left(90)
        rin(d, n)
        turtle.right(90)
        if n != 1 and n != 2:
            rin(d, n)



def main():
    d = int(input('Длина стороны:'))
    n = int(input('Глубина рекурсии:'))
    turtle.speed(0)
    rin(d, n)
    turtle.mainloop()

if __name__ == "__main__":
    main()
