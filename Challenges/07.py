"""
When working in a global environment, you’ll have to present information in both metric 
and Imperial units. And you’ll need to know when to do the conversion to ensure the most 
accurate results.
Create a program that calculates the area of a room. Prompt the user for the length and 
width of the room in feet. Then display the area in both square feet and square meters.

Input: length, width
Process: Calculate area
Output: Square feet, square meters

"""

CONST = 0.09290304

def calculate_area(length,width):
    return length*width

def calculate_square_meters(length,width):
    return length*width*CONST

def show_result(length, width):
    print(f"You entered dimensions of {length} feet by {width} fee")
    print(f"The area is {calculate_area(length,width)} square feet")
    print(f"{calculate_square_meters(length,width)} square meters")

length = float(input("What is the length of the room in feet?"))
width = float(input("What is the width of the room in feet?"))

show_result(length,width)



