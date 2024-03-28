"""
You don’t always need a complex control structure to solve
simple problems. Sometimes a program requires an extra
step in one case, but in all other cases there’s nothing to do.
Write a simple program to compute the tax on an order
amount. The program should prompt for the order amount
and the state. If the state is “WI,” then the order must be
charged 5.5% tax. The program should display the subtotal,
tax, and total for Wisconsin residents but display just the
total for non-residents.

Input:  order amount, state
Process: Compute the tax
Output: Subtotal, tax, total (WI) / total (NR)

- How to get the porcentage of a value
Convierte el porcentaje a su forma decimal: Divide el porcentaje entre 100 para obtener su equivalente decimal. Por ejemplo, 10% se convierte en 0.10.
Calcula el impuesto: Multiplica el valor del producto por el porcentaje de impuesto en su forma decimal. Siguiendo el ejemplo anterior:

- How to compare strings

"""
import math

def applied_tax(amount):
    return float((5.5/100))

def get_total(order_amount, state):
    if state.lower() == "wi":
        return (applied_tax(order_amount)*order_amount)+order_amount
    else:
        return order_amount

def print_order_details(amount, state):
    if state.lower() == "wi":
        print(f"The subtotal is ${amount}")
        print(f"The tax is ${applied_tax(amount)}")
        print(f"The total is ${get_total(amount, state)}")
    else:
        print(f"The total is ${amount}")


order_amount = int(input("What is the order amount? "))
state = input("What is the state? ")

print_order_details(order_amount,state)


    