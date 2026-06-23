r = int(input("Enter the radius of the circle:"))

import turtle

turtle.Screen().title('Circle')

turtle.Screen().setup(700,700)

d = turtle.Turtle()

d.circle(r * 10)

Area = 3.14 * r**2

Perimeter = 6.28 * r 

print( "Area of the circle is {} and Perimeter is {}".format(Area, Perimeter))

turtle.exitonclick()