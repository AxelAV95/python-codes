"""
Division isn’t always exact, and sometimes you’ll write programs that will need to deal with the 
leftovers as a whole number instead of a decimal.
Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, 
and the number of slices per pizza. Ensure that the number of pieces comes out even. Display the 
number of pieces of pizza each person should get. If there are leftovers, show the number of 
leftover pieces.

Input: number of people, number of pizzas, number of slices per pizza
Process: Calculate number of pieces
Output: pieces per person, leftover
"""

people = input("How many people?")
pizzas = input("How many pizzas do you have?")
slices = input("How many slices per pizza?")

if people.isdigit() and pizzas.isdigit() and slices.isdigit():
    people = int(people)
    pizzas = int(pizzas)
    slices = int(slices)

    total = pizzas*slices
    per_person = total//people
    leftover = total%people

    print(f"{people} people with {pizzas} pizzas")
    print(f"Each person gets {per_person} pieces of pizza. There are {leftover} leftover pieces.")
else:
    print("Por favor, ingresa un valor entero válido.")
    exit()