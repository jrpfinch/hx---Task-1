# Task 1 - Circle Properties Challenges - solution

# Import the math library
import math

#print (math.pi)

# Write a program that:
# - Asks the user to enter the diameter of a cirlce
diameter = int(input("Enter the diameter of the circle: "))

# - Outputs the radius of the circle (diameter divided by 2)
radius = diameter/2
print(f"The radius of the circle is: {radius}")

# - Outputs the area of the circle (Pi multiplied by the radius squared)
area = math.pi * (radius * radius)
print(f"The area of the circle is: {area:.2f}")


# - Outputs the circumference of the circle (Pi multiplied by the diameter)
circumference = math.pi*diameter
print(f"The circumference of the circle is: {circumference:.2f}")

# - Asks the user to enter the arc angle
arc = int(input("Enter the arc angle: "))

# - Outputs the arc length (circumference multiplied by the arc angle, divided by 360)
arc_length = (circumference * arc)/360
print(f"The arc length is: {arc_length:.2f}")

# NOTE: The syntax to use Pi is math.pi