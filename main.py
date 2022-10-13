# Task 1 - Circle Properties Challenges

# Import the math library
import math

#print (math.pi)

# Write a program that:
# - Asks the user to enter the diameter of a cirlce
diameter = float(input("Please enter a circle diameter: "))

# - Outputs the radius of the circle (diameter divided by 2)
print(f"The radius is {diameter/2}")


# - Outputs the area of the circle (Pi multiplied by the radius squared)
print(f"The area is {math.pi*(0.5*diameter)**2}")


# - Outputs the circumference of the circle (Pi multiplied by the diameter)
circumf = math.pi*diameter
print(f"The circumference is {circumf}")


# - Asks the user to enter the arc angle
arc_angle = float(input("Please enter the arc angle: "))


# - Outputs the arc length (circumference multiplied by the arc angle, divided by 360)
print(f"Arc length = {(arc_angle/360)*circumf}")



# NOTE: The syntax to use Pi is math.pi