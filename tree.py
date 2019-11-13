import turtle


def draw_brach(brach_length):
    if brach_length > 5:
        if brach_length < 40:
            turtle.color('blue')
        else:
            turtle.color('black')
        turtle.forward(brach_length)
        turtle.right(25)
        draw_brach(brach_length - 15)
        turtle.left(50)
        draw_brach(brach_length - 15)
        if brach_length < 40:
            turtle.color('blue')
        else:
            turtle.color('orange')
        turtle.right(25)
        turtle.backward(brach_length)


def main():
    turtle.bgcolor('purple')
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')
    draw_brach(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()