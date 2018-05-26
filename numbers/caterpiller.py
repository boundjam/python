import random
import turtle as t


def caterpiller():
    t.bgcolor('yellow')
    caterpiller = t.Turtle()
    caterpiller.shape('square')
    caterpiller.color('red')
    caterpiller.speed(0)
    caterpiller.penup()
    caterpiller.hideturtle()


def leaf():
    leaf = t.Turtle()
    leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20),
                (6, 18), (2, 14))
    t.register_shape('leaf', leaf_shape)
    leaf.shape('leaf')
    leaf.color('green')
    leaf.penup()
    leaf.hideturtle()
    leaf.speed(0)


def text_function():
    game_started = False
    text_turtle = t.Turtle()
    text_function.write('Press SPACE to start', align = 'center',font = ('Arial',16,'bold'))
    text_turtle.hideturtle()


def score_function():
    score_turtle = t.Turtle()
    score_turtle.hideturtle()
    score_turtle.speed(0)


def outside_window():
    pass


def game_over():
    pass


def display_score(current_score):
    pass


def place_leaf():
    pass


def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    caterpiller.speed = 2
    caterpiller.length = 3
    caterpiller.shapesize(1,caterpiller,1)
    caterpiller.showturtle()
    display_score(score)
    place_leaf()


def main():
    caterpiller()
    leaf()
    text_function()
    score_function()


if __name__ == '__main__':
    main()