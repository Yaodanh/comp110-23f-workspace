"""TODO: Describe your scene program."""
 
__author__ = "730707593"
from turtle import Turtle, done


def draw_sun(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a sun."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red") 
    turtle.circle(radius)
    turtle.end_fill()


def draw_mountains(turtle: Turtle) -> None:
    """Draw a mountain."""
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("gray")
    idx: int = 0
    while idx < 3:
        turtle.forward(200)
        turtle.left(120)
        idx += 1
    turtle.end_fill()


def draw_tree(turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("brown")
    turtle.goto(x - 20, y - 40)
    turtle.goto(x + 20, y - 40)
    turtle.goto(x, y)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green") 
    turtle.circle(20)
    turtle.end_fill()


def draw_ground(turtle: Turtle) -> None:
    """Draw a ground."""
    turtle.penup()
    turtle.goto(-400, -200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green") 
    turtle.goto(400, -200)
    turtle.goto(400, -400)
    turtle.goto(-400, -400)
    turtle.goto(-400, -200)
    turtle.end_fill()


def main() -> None:
    """Draw a landscape."""
    leo: Turtle = Turtle()
    leo.speed(0)
    leo.hideturtle()

    # Draw a sun
    draw_sun(leo, 300, 300, 30)

    # Draw mountains
    draw_mountains(leo)
    leo.color("black")

    # Draw trees
    for x in [-200, -100, 0, 100, 200]:
        draw_tree(leo, x, -100)

    # Draw a ground
    draw_ground(leo)
    done()


if __name__ == "__main__":
    main()
    