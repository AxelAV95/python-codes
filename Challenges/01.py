"""
The “Hello, World” program is the first program you learn
to write in many languages, but it doesn’t involve any input.
So create a program that prompts for your name and prints
a greeting using your name.
"""

"""
Input: Name
Processes: Print
Output: Greeting
"""

name = input("What is your name?")
greeting = f"Hello, {name}, nice to meet you"

print(greeting)

#Version 2
print("What is your name? ", end="")
print("Hello, " + input() + ", nice to meet you!")

#Version 3
name_v2 = input("What is your name?")

if name_v2 == "Sherry":
    print(f"Good morning, {name_v2}, nice to meet you")
if name_v2 == "Axel":
    print(f"Hello, {name_v2}, nice to meet you")
if name_v2 == "Maria":
    print(f"Good evening, {name_v2}, nice to meet you")



