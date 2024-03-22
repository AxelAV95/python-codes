"""
Sometimes you have to round up to the next number rather
than follow standard rounding rules.
Calculate gallons of paint needed to paint the ceiling of a
room. Prompt for the length and width, and assume one
gallon covers 350 square feet. Display the number of gallons
needed to paint the ceiling as a whole number

input: length, width
processes: calculate total of gallons
output: total

"""
import math

square_feet = 350

length = float(input("Ingrese la longitud de la habitación en pies: "))
width = float(input("Ingrese el ancho de la habitación en pies: "))

area = int(length)*int(width)

gallons = math.ceil(area / square_feet)

# Mostrar el resultado
print("Necesitarás comprar", gallons, "galones de pintura para cubrir", area, "pies cuadrados.")

