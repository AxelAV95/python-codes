"""
Create a program that prompts for an input string and 
displays output that shows the input string and the number of
characters the string contains.

Input: string
Processes: Show, Count
Output: string, number of characters

"""

def count(string):
    return len(string)

string = input("What is the input string")

if len(string) == 0:
    print("Must enter some string")
else:
    total = count(string)
    print(f"{string} has {total} characters")
