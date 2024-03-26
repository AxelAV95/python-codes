"""
Simple interest is something you use only when making a
quick guess. Most investments use a compound interest
formula, which will be much more accurate. And this formula requires you to incorporate exponents into your programs.
Write a program to compute the value of an investment
compounded over time. The program should ask for the
starting amount, the number of years to invest, the interest
rate, and the number of periods per year to compound.

input = starting amount, years of investment, interest rate, number of periods per year
processes = calculate compound interest
output = total invested


"""
import math

def calculateCompoundInterest(p,r,t,n):
    return p * pow((1 + ((r/100)/n)),(n*t))

p = int(input("What is the principal amount? "))
r = float(input("What is the rate? "))
t = int(input("What is the number of years? "))
n = int(input("What is the number of times the interest is compounded per year? "))

compound = round(calculateCompoundInterest(p,r,t,n),2)
print(f"${p} invested at {r}% for {t} years compounded {n} times per year is ${compound}")

