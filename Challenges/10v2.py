tax_rate = 5.5 / 100
subtotal = 0

# Bucle para ingresar los artículos
while True:
    item_price = input("Enter the price of the item (or 'done' to finish): ")
    if item_price.lower() == 'done':
        break
    item_quantity = int(input("Enter the quantity of the item: "))
    subtotal += float(item_price) * item_quantity

# Calcular impuestos y totales
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

# Imprimir resultados
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
