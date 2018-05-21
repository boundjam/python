import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.speed('slow')
    t.pensize(1)
    t.start_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
    t.end_fill()
    t.penup()
t.goto(0,0)