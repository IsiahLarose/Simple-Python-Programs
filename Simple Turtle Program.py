#Isiah Larose
# CS100 Sec 037
# HW3 Sept, 17, 2019

import turtle
import math
aScreen =  turtle.Screen()
shelly = turtle.Turtle()
shelly.width(5)
shelly.color("Blue")
turtle.bgcolor("Yellow")
shelly.left(180)
shelly.forward (100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.color("Green","Purple")
shelly.penup()
shelly.pendown()
shelly.left(120)
shelly.forward(100)
shelly.left(120)
shelly.forward(100)
shelly.left(120)
shelly.forward(100)

shelly.color("purple")
shelly.pendown()
shelly.left(90)
shelly.right(60)
shelly.forward(100)
shelly.right(100)
shelly.right(120)
shelly.right(75)
shelly.forward(90)
shelly.left(75)
shelly.forward(100)
shelly.left(75)
shelly.forward(75)
shelly.left(56)
shelly.forward(98)
shelly.color("red")
shelly.pendown()

shelly.clear()

for diameter in range(200):
    turtle.dot(diameter, 'blue')
turtle.dot(diameter -1, 'white')

for diameter in range(150):
    turtle.dot(diameter, 'blue')
    turtle.dot(diameter -1, 'white')

for diameter in range(100):
    turtle.dot(diameter, 'blue')
    turtle.dot(diameter -1, 'white')

for diameter in range(50):
    turtle.dot(diameter, 'blue')
    turtle.dot(diameter -1, 'white')
    turtle.hideturtle()
    turtle.mainloop()

x = math.log2(1000000)
print ("The value of 100 log base 2 of 1 million is:",x)
j = [math.factorial(100)]
print ("100! is equal to",j)
k = math.gcd(63,49)
print("The greatest common divisor of 63 and 49 is:", k)



