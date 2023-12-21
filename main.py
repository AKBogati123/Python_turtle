# from turtle import Turtle,Screen 

# timmy_the_turtle = Turtle()
# screen = Screen()
# timmy_the_turtle.color("red")
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# screen.mainloop()
# import turtle as t
# import random

# tim = t.Turtle()
# screen = t.Screen()  # Use 't.Screen()' instead of 'Screen()'

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# screen.exitonclick()  # Use 'screen.exitonclick()' to close the window on click



# import turtle as t
# import random

# tim = t.Turtle()
# screen = t.Screen()  # Use 't.Screen()' instead of 'Screen()'

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed"]
# directions = [0, 90, 180, 270]
# tim.pensize(5)

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
    
# screen.exitonclick()


# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# screen = t.Screen()  # Use 't.Screen()' instead of 'Screen()'

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
    
# directions = [0, 90, 180, 270]
# tim.pensize(5)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
    
# screen.exitonclick()


# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# screen = t.Screen()  # Use 't.Screen()' instead of 'Screen()'

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
# tim.speed("fastest")

# def draw_spirograph(size_of_graph):
#   for _ in range(int(360 / size_of_graph)):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + size_of_graph)

# draw_spirograph(5)
# screen.exitonclick()

import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
