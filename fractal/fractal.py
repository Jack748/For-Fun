import turtle
import time

t = turtle.Turtle()
t.left(90)
t.speed(0)



def draw(len):
    if len > 8:
        t.forward(len)
        t.left(30)
        draw(len/1.3)
        t.right(60)
        draw(len/1.3)
        t.left(30)
        t.backward(len)


draw(50)

time.sleep(2)
