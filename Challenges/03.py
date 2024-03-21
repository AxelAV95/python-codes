"""
Quotation marks are often used to denote the start and end
of a string. But sometimes we need to print out the quotation
marks themselves by using escape characters.
Create a program that prompts for a quote and an author.
Display the quotation and author as shown in the example
output.

Input: quote, author
Processes: Display quote and author
Output: Quote, author

"""

quote = input("What is the quote? ")
author = input("Who said it? ")
output = author + ' says, "' + quote + '"'

print(output)