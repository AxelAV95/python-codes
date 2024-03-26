"""
Computing simple interest is a great way to quickly figure
out whether an investment has value. It’s also a good way
to get comfortable with explicitly coding the order of operations in your programs.
Create a program that computes simple interest. Prompt for
the principal amount, the rate as a percentage, and the time,
and display the amount accrued (principal + interest).
The formula for simple interest is
A = P(1 + rt), where P is
the principal amount, r is the annual rate of interest, t is the
number of years the amount is invested, and A is the amount
at the end of the investment.

input = principal amount, percentage, time
process = compute simple interest
output = amount (principal + interest)
"""

import math

def calcultateSimpleInterest(principal, rate, time):
    return principal*((rate/100)*time)

principal = int(input("Enter the principal:"))
rate = float(input("Enter the rate of interest:"))
time = int(input("Enter the number of years:"))

total = principal+calcultateSimpleInterest(principal, rate, time)

print(f"After {time} years at {rate}%, the investment will be worth ${math.ceil(total)}.")

