import random
# word selection
word = ('apple', 'orange', 'pear', 'glass of milk', 'otter', 'snake', 'iguana', 'tiger', 'eagle')
selectword = random.choice(word)

# grammatical rules
vowel = ('a', 'e', 'i', 'o', 'u')

# test random selection a or an rules
selectword
if selectword[0].startswith(vowel):
    print("an " + selectword)
else:
    print("a " + selectword)

#test input an / a rule
#animal = input("Type an animal here: ")
#if animal[0].startswith(vowel):
#    print("You are walking down the road when an " + animal + " jumps out of the bush")
#else:
#    print("You are walking down the road when a " + animal + " jumps out of the bush")
