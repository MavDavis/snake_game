# import turtle
# import time

# wn = turtle.Screen()
# wn.title("Mavdavis snake game")
# wn.bgcolor("green")  # Set the background color to green
# wn.setup(width=600, height=600)
# wn.tracer(0)
# print(wn)

# # Your game logic goes here
# head = turtle.Turtle()
# head.speed(0) 
# head.color("black") 
# head.penup() 
# head.goto(0,0)
# head.direction = "stop"

# wn.update()  # Refresh the screen

# wn.mainloop()
# time.sleep(1)
import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)
# Close the turtle graphics window when clicked
turtle.done()
