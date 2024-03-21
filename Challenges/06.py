"""
Your computer knows what the current yearis, which means
you can incorporate that into your programs. You just have
to figure out how your programming language can provide
you with that information.
Create a program that determines how many years you have
left until retirement and the year you can retire. It should
prompt for your current age and the age you want to retire
and display the output as shown in the example that follows.

Input: current age, retire age
Process: Calculate
Output: retirement left years
"""

import datetime

def difference_year(current, retire):
    return int(retire) - int(current)

current_age = input("What is your current age?")
retire_age = input("At what age would you like to retire? ")

output = f"You have {difference_year(current_age,retire_age)} years left until you can retire. It's {datetime.datetime.now().year}, so you can retire in {datetime.datetime.now().year+difference_year(current_age,retire_age)}."

print(output)