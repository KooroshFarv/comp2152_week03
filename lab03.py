
# gblearn : 
# login
# cd .python


import random

# Dice options


diceOpt = list(range(1,7))

weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nucleaer Bomb']

print("Available Weapons" , ' ', weapons)


def get_combat_strength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <=6:
            return value
        else:
            print('Invalid input! Enter a number between 1 - 6')

combatStrength = get_combat_strength("Enter your combat strength 1-6")


for j in range(1, 21, 2):
    heroRoll = random.choice(diceOpt)
    monsterRoll = random.choice(diceOpt)


    heroWeapon = weapons[heroRoll - 1]
    MonsterWeapon = weapons[monsterRoll - 1]
    heroTotal = combatStrength + heroRoll
    monsterTotall = combatStrength + monsterRoll