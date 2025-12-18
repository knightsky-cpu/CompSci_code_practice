import time

name = input("What is Your name traveler?: ")
time.sleep(2)

def class_role():
    choose_class = input("What class will you choose? Knight? Mage? Rouge?: ")
    character_type = choose_class
    if choose_class != "knight" and choose_class != "Knight" and choose_class != "mage" and choose_class != "Mage" and choose_class != "rouge" and choose_class != "Rouge":
        print("that is not a recognized class, please try again")
        return class_role()
    return character_type

character_type = class_role()
time.sleep(2)

strenght = 5
dexterity = 5
wisdom = 5
constitution = 5
luck = 2

if character_type == "knight" or character_type == "Knight":
    print(f"you are a {character_type}")
    time.sleep(2)
    print("your stats are: str:", (strenght + 5), "dex:", (dexterity - 1), "wis:", (wisdom - 1), "con:", (constitution + 5), "luck:", luck)
elif character_type == "mage" or character_type == "Mage":
    print(f"you are a {character_type}")
    time.sleep(2)
    print("your stats are: str:", (strenght - 2), "dex:", (dexterity), "wis:", (wisdom + 5), "con:", (constitution - 1), "luck:", luck + 2)
elif character_type == "rouge" or character_type == "Rouge":
    print(f"you are a {character_type}")
    time.sleep(2)
    print("your stats are: str:", (strenght), "dex:", (dexterity + 5), "wis:", (wisdom + 2), "con:", (constitution - 1), "luck:", luck + 4)





