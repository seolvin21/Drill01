import turtle

def turtle_move(direction):
    turtle.setheading(direction)
    turtle.forward(50)
    turtle.stamp()
    
def restart():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(lambda: turtle_move(90),'w')
turtle.onkey(lambda: turtle_move(180),'a')
turtle.onkey(lambda: turtle_move(270),'s')
turtle.onkey(lambda: turtle_move(0),'d')
turtle.onkey(restart,'Escape')
turtle.listen()
