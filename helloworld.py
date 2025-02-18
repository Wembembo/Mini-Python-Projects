import random

race_list = "human", "orc", "elf", "dwarf", "humonculous", "sea creature", "dungeon master"

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
print()
age = (input("How old are you? "))
print()
print("You can pick one of the following races: ", race_list)
while True:
    try:
        race = input("Choose a race:")
        if race in race_list:
            break
        else:
            print("Select a listed race, dumb dumb")
    except:
        continue

print()

name = first_name + " " + last_name
print(("your name is:"),(name))
print(("aged:"),(age))
print(("race: "), (race))
print()

print("Time to roll some stats! Let's start with luck. ")
print()

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_luck = 0
while True:
    try:
        rp_luck = random.randint(1, 20)
        print("You rolled", rp_luck,("for luck"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_luck = random.randint(1, 20)
            print("You rolled", rp_luck,("for luck"))
            break
        else:
            break
    except:
        continue
print(f"Your luck is: {rp_luck}")
print()
print("Next, we'll roll for strength")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_str = 0
while True:
    try:
        rp_str = random.randint(1, 20)
        print("You rolled", rp_str,("for strength"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_str = random.randint(1, 20)
            print("You rolled", rp_str,("for strength"))
            break
        else:
            break
    except:
        continue
print(f"Your strength is: {rp_str}")
print()
print("Next, we'll roll for agility")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_agl = 0
while True:
    try:
        rp_agl = random.randint(1, 20)
        print("You rolled", rp_agl,("for agility"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_agl = random.randint(1, 20)
            print("You rolled", rp_agl,("for agility"))
            break
        else:
            break
    except:
        continue
print(f"Your agility is: {rp_agl}")
print()
print("Next, we'll roll for constitution")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_con = 0
while True:
    try:
        rp_con = random.randint(1, 20)
        print("You rolled", rp_con,("for constituion"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_con = random.randint(1, 20)
            print("You rolled", rp_con,("for constituion"))
            break
        else:
            break
    except:
        continue
print(f"Your constituion is: {rp_con}")
print()
print("Next, we'll roll for charisma")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_chr = 0
while True:
    try:
        rp_chr = random.randint(1, 20)
        print("You rolled", rp_chr,("for charisma"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_con = random.randint(1, 20)
            print("You rolled", rp_chr,("for charisma"))
            break
        else:
            break
    except:
        continue
print(f"Your charisma is: {rp_chr}")
print()
print("Next, we'll roll for intelligence")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_int = 0
while True:
    try:
        rp_int = random.randint(1, 20)
        print("You rolled", rp_int,("for intelligence"))
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_con = random.randint(1, 20)
            print("You rolled", rp_int,("for charisma"))
            break
        else:
            break
    except:
        continue
print(f"Your intelligence is: {rp_int}")
print()
print("Next we'll roll for dick size")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_dik = 0
while True:
    try:
        rp_dik = random.randint(1, 20)
        print("You rolled", rp_dik,("for dick size"))
        if rp_dik == 20:
            print("damn", "nice cock bro")
        reroll = input("Would you like to reroll? You can only do this once? y/n?: ")
        reroll=reroll.replace("y", "Y")
        if reroll == "Y":
            rp_con = random.randint(1, 20)
            print("You rolled", rp_dik,("for dick size"))
            break
        else:
            break
    except:
        continue
print()
print()
print()
print("To summarise, here's your character:"),
print(("name: "),(name))
print(("age: "),(age))
print(("race: "),(race))
print(("luck: "),(rp_luck))
print(("Strength: "),(rp_str))
print(("Agilty: "),(rp_agl))
print(("Constitution: "),(rp_con))
print(("Charisma: "),(rp_chr))
print(("Intelligence: "),(rp_int))
print("Dick size: Nice")

while True:
   answer = input('Happy with everything?:')
   if answer.lower().startswith("y"):
      print("Then let your adventure begin:")
      break
   elif answer.lower().startswith("n"):
      print("ok, bitch, start over: ")
      exit()

print("Your jorney starts with you waist deep in a bog, beside you are a map and an upside down mule with its legs "
      "poking out of the mud.")
print()
map = input("The map is in reach, but it is very muddy and possibly wet, would you like to grab the map? y/n: ")
print()
print()
map = map.replace("y","Y")
if map == "Y":
    print("You obtained the map! It WAS muddy, and only slightly wet. Damp, really.")
    print()
    print("You put the map in your pocket, which has now also become slightly muddy and damp.")
else:
    print("You left the map, probably wasn't worth the paper it was printed on anyway.")
print()
print("To your right is the upside down mule, he is very handsome, as far as mules go anyway.")
print()
print("roll for charisma: ")

while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_mule = rp_chr + 3
print(f"you rolled a", rp_mule)
if rp_mule <=6:
    print("The mule is not impressed, there's going to be no more mule fuel for you.")
elif rp_mule >=7 or rp_mule <= 15:
    print("The mule is cautious, but curious about you. And the mule can't say no, because of the implication")
else:
    print("The mule winks at you, a feat that you have never seen before. This is no mule, this is a night-mare!")
print()
print("with the mule by your side you drag yourself out of the bog and go home to Hull, another bog.")
print()

print("you make your way back to Hull, and you are accosted by a local asbo, it sounds like he's trying to communicate "
      "in English but you can't be quite sure")
print()
print("You try to understand the asbo, roll for intelligence")
while True:
    try:
        roll = int(input("Pick a number between 1-10, this is how hard you roll the d20: "))
        if roll <=0 or roll >=11:
            print("You rolled that wrong, how did you do that?")
            print("try again")
        else:

            break
    except:
        continue
rp_asbo = int(rp_int) + 4
print((f"You rolled a: "),rp_asbo)
if rp_asbo <=19:
    print("You failed to understand the asbo, he begins shouting. You flee.")
else:
    print("The asbo is surprisingly well spoken, he seems lost and hungry. You give him the mule for fuel.")

print("The End..?")