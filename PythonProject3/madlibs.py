# Project: Mad libs game

# How to play
# Mad Libs is a simple game where a player write a bunch of
# words to complete a story with some blank spaces.

# First of all, I will make input to ask a
# player to write any word in parts of speech
# (noun, adjective, verb)

# To do that, I'll transform input as a variable to become
# better our understanding.

noun1 = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb ending in 'ING': ")
city = input ("Enter a city: ")

print(f"Today I was {verb} and suddenly saw {noun1} in {city}.")
print(f"I got surprised, because {noun1} was very {adjective}.")
print(f"What a {adjective2} day !")

# As you can see, a player can type anything and make an
# unexpected story.
# This is a very simple projects that involves variables,
# f-strings and input.
