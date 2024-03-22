"""
At some point, you might have to deal with currency
exchange rates, and you’ll need to ensure your calculations
are as precise as possible.
Write a program that converts currency. Specifically, convert
euros to U.S. dollars. Prompt for the amount of money in
euros you have, and prompt for the current exchange rate
of the euro. Print out the new amount in U.S. dollars. 

input: money(euros), exchange rate of euro
processes: Convert currency
output: new amount in dollars

"""
# Prompt for the amount of money in euros and the current exchange rate
euros = float(input("How many euros are you exchanging? "))
exchange_rate_euro_to_usd = float(input("What is the exchange rate? "))

# Calculate the amount in U.S. dollars
usd = euros * exchange_rate_euro_to_usd

# Print out the new amount in U.S. dollars
print(f"{euros} euros a un tipo de cambio de {exchange_rate_euro_to_usd} es {usd:.2f} USD.")

