"""
Use boolean variables to control program logic between two different code
paths.
"""


if __name__ == '__main__':
    from tkinter import Tk, messagebox
    import turtle
    window = Tk()
    window.withdraw
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    weekend = True
    weekend2 = False
    if weekend:
        messagebox.showinfo(title=None, message='It is not the weekend.')
    if weekend2:
        messagebox.showinfo(title=None, message='It is the weekend.')
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passed = True
    failed = False
    if passed:
        messagebox.showinfo(title=None, message='You passed!')
    if failed:
        messagebox.showinfo(title=None, message='Ypu failed.')
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    over = True
    over2 = False
    if over:
        messagebox.showinfo(title=None, message='Game over')
    if over2:
        messagebox.showinfo(title=None, message='Game not over.')
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    red = True
    square = True
    window = turtle.Screen()
    window.bgcolor('white')
    my_turtle = turtle.Turtle()
    if red:
        my_turtle.color('red')
    if square:
        my_turtle.begin_fill()
        for i in range(4):
            my_turtle.forward(50)
            my_turtle.left(90)
        my_turtle.end_fill()

    pass
