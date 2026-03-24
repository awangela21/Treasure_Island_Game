print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You\'re at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake. '
                     'There is an island in the middle of the lake.'
                     'Type "wait" to wait for a boat. '
                     'Type "swim" to swim across.'
                     'Type "cross" to cross the old bridge\n').lower()

    if choice_2 == "wait":
        choice_3 = input ('You arrive at the island unharmed. There is a house with 3 doors.'
                          'One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if choice_3 == "red":
            print("You have fallen into an active volcano!")
        elif choice_3 == "blue":
            print("You have fallen into a river full of piranhas!")
        elif choice_3 == "yellow":
            print("Congratulations! You have found the treasure!")
        else:
            print("You chose a door that does not exist! You have fallen into the abyss")
    if choice_2 == "cross":
        choice_3 = input('Under the bridge lives a troll. Fight, flight, bribe or beg?\n')
        if choice_3 == "flight":
            print("The troll catches up to you and swallows you whole!")
        elif choice_3 == "fight":
            print('You have defeated the troll but died of your injuries')
        elif choice_3 == "bribe":
            print("You have survived but lost all chances of finding the treasure. "
                  "Moreover,the troll have robbed you blind leaving you destitute")
        elif choice_3 == "beg":
            print("Annoyed by your cries, the troll decides to barbecue you")
        else:
            print("The choice does not exist! The troll decides to broil you")
    if choice_2 == "swim":
        print("Ferocious mermaids have drowned you!")

if choice_1 == "right":
    print("You are eaten by a monster crocodile. You died")


