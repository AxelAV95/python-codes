"""
Working with multiple inputs and currency can introduce
some tricky precision issues.
Create a simple self-checkout system. Prompt for the prices
and quantities of three items. Calculate the subtotal of the
items. Then calculate the tax using a tax rate of 5.5%. Print
out the line items with the quantity and total, and then print
out the subtotal, tax amount, and total.


input: prices, quantities
processes: calculate subtotal, calculate tax
output: items with quantity and total, subtotal, tax amount and total

"""

tax = (5.5/100)

item_price_1 = int(input("Enter the price of item 1: "))
item_quantity_1 = int(input("Enter the quantity of item 1: "))
item_price_2 = int(input("Enter the price of item 2: "))
item_quantity_2 = int(input("Enter the quantity of item 2: "))
item_price_3 = int(input("Enter the price of item 3: "))
item_quantity_3 = int(input("Enter the quantity of item 3: "))

subtotal = float((item_price_1*item_quantity_1)+(item_price_2*item_quantity_2)+(item_price_3*item_quantity_3))
tax_applied = float(subtotal*tax)
total = float(subtotal+tax_applied)

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax_applied}")
print(f"Total: ${total}")