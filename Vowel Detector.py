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

####################################madlib generator####################################################################
#print("This is a mad lib, we're going to enter some words and see what comes out. \n")
#print("this one is called, A Letter from Camp. \n")
#print("Now, lets pick some words.")

#relative_1 = input("Choose a relative: ")
#adj_1 = input("Pick your first adjective (eg: rotten): ")
#adj_2 = input("Pick your second adjective (eg: rotten): ")
#adj_3 = input("Pick your third adjective (eg: rotten): ")
#room_1 = input("Enter the name of someone in the room with you: ")
#adj_4 = input("Pick your fourth adjective (eg: rotten): ")
#adj_5 = input("Pick your fifth adjective (eg: rotten): ")
#verb_1 = input("Pick a verb ending in 'ed' (eg: Played): ")
#ed verb
#bodypart = input("Pick a body part: ")
#verb_2 = input("Pick another verb, this time ending in 'ing' (eg: Playing): ")
#ing verb
#noun_1 = input("We'll now need a plural noun (eg: footballs): ")
#plural noun
#noun_2 = input("We'll now need a singular noun (eg: gun): ")
#singular noun
#adverb = input("We now need an adverb (eg: hypnotically): ")
#verb_3 = input("We need another verb, this time in present tense (eg: play): ")
#verb_4 = input("We need ANOTHER verb, this time in present tense (eg: play): ")
#relative_2 = input("Choose another relative: ")
#room_2 = input("Lastly, enter the name of someone else in the room with you: ")

#print("Thanks for doing that, lets take a look at what came out: \n")

#print("Dear " + relative_1 + ",\n")
#print("I am having a " + adj_1 + " time at camp.\n")
#print("The counselour is " + adj_1 + " and the food is " + adj_3 + ". I met " + room_1 + " and we became " + adj_4
#+ " friends.\n")
#print("Unfortunately, " + room_1 + " is " + adj_5 + " and I " + verb_1 + " my " + bodypart + " so we couldn`t go " ,
#verb_2 + " like everybody else.\n")
#print("I need more " + noun_1 + " and a " + noun_2 + " sharpener, so please " + adverb, verb_3 + " more when you ",
#      verb_4 + "back.\n")
#print("Your" + relative_2 + ",\n")
#print(room_2 + ".")



