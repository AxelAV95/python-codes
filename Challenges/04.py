"""
Mad libs are a simple game where you create a story template with blanks for words. You, or 
another player, then construct a list of words and place them into the story, creating an 
often silly or funny story as a result. Create a simple mad-lib program that prompts for a noun,
a verb, an adverb, and an adjective and injects those into a
story that you create.

Input: noun, verb, adverb, adjective
Processes: create
Output: story
"""

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
story = f"Do you {verb} your {adjective} {noun} {adverb} ? That's hilarious!"

print(story)