"""
You’ll often write programs that deal with numbers. And
depending on the programming language you use, you’ll
have to convert the inputs you get to numerical data types.
Write a program that prompts for two numbers. Print the
sum, difference, product, and quotient of those numbers as
shown in the example output:

Input: number one, number two
Processes: Sum, difference, product, quotient
Output: results
"""

def check_negative(number):
    return number < 0

def solicitar_numero():
    return input("Enter a number: ")

def sum(num1,num2):
    return num1+num2

def difference(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def convertir_a_numero(valor):
    try:
        return int(valor)
    except ValueError:
        print("Error: Please enter a numeric value.")
        return None

num1 = solicitar_numero()
num2 = solicitar_numero()

num1 = convertir_a_numero(num1)
num2 = convertir_a_numero(num2)

if num1 is not None and num2 is not None:
    if check_negative(num1)== True or check_negative(num2) == True:
        print("Please insert only positive numbers")
    else:
        print(f"{num1} + {num2} = {sum(num1,num2)} \n")
        print(f"{num1} - {num2} = {difference(num1,num2)} \n")
        print(f"{num1} * {num2} = {multiply(num1,num2)} \n")  