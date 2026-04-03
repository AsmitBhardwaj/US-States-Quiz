import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#mouse coordinates
def get_mouse_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_coor)
turtle.mainloop()

screen.exitonclick()