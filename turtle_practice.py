import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(12)

    angie = turtle.Turtle()
    angie.speed(100)
    angie.color("white")

    julie = turtle.Turtle()
    julie.speed(50)

 
    for k in range (0,8):
        angie.left(80)
        for m in range (0,10):
            angie.right(10)
            for l in range (10):
                angie.forward(20)
                angie.right(10)
    window.exitonclick()

if __name__ == '__main__':
    draw_art()
