import random

location = ["at work", "at home", "at school,", "at the store", "on a bus", "on a train", "on a skateboard",
            "at a morgue",
            "in jail"]
villain = ["witch", "murderer", "coworker", "salesman", "priest", "doctor", "man", "woman", "Guilty Gear player",
           "Fox main", "Falco main", "lizard", "creature"]
descriptor_1 = ["small", "large", "average sized", "wide", "oddly narrow", "odd looking", "freakish", "funny sounding",
                "large headed", "purpose driven", "hard working", "grotesque", "lazy"]
descriptor_2 = ["green", "yellow", "pink", "blue", "red", "invisible", "hairy"]
verb_1 = ["holding", "brandishing", "sucking on", "licking", "wearing", "playing with", "stroking"]
obj = ["a gun", "a cross", "a small vampire", "several tooth picks", "a Nintendo Gamecube controller",
       "a bottle of Sprite", "a wallet"]
attachment = ["on", "around", "across", "over"]
body_part = ["neck", "arm", "hand", "foot", "face", "leg", "chest", "head"]

print("Welcome to Tim's hypothetical scenario generator!")
print("This generator allows you to come up with 'Tim like' scenarios \n\n")

#name = input("Enter your first name: ")
#print(("Thank you,"),name,("."))

print("You're", random.choice(location), "and a", random.choice(descriptor_1), random.choice(descriptor_2),
      random.choice(villain), "approaches you")
action = random.choice(verb_1)
verbline = "they are " + action + " " + random.choice(obj)

if action == "wearing":
    verbline += f" {str(random.choice(attachment))} their {str(random.choice(body_part))}"

print(verbline)