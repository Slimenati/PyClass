TensionPoints = 0
import random

#monster information
monster_name = "Goblin"
monster_health = 50
player_health = 50
monster_damage = 2
print(f"You are now fighting {monster_name}! It has {monster_health} health.")
print(f"You have {player_health} health.")

while monster_health > 0 and player_health > 0:
    #Print the possible moves the user can do
    print("You can select one of the following moves:")
    print("slash (1-10 damage)")
    print("stab (4-16 damage)")
    print("""defend (You take the half the damage you would normally take)
(You also gain 10 Tension Points (TP).""")
    print("dodge (Both sides take no damage) (You also gain 5 TP.)")
    print("fireball (requires 20 TP) (Deals 25-30 damage)")
    print("heal prayer (requires 15 TP) (Heals 8 health)")
    print("")
    
    #Ask the user to select a move and store as variable
    move = input("Choose the move you like to use: ")
    
    #The damage the monster deals
    
    monster_damage = random.randint(4, 7)
    if monster_health < 20:
        print(f"{monster_name} became enraged! It will now deal triple the damage.")
        monster_damage = monster_damage * 3
    else:
        chance = random.randint(1, 2)
    if chance == 2:
        print(f"{monster_name} is preparing something...")
    
    #What happens for each move
    if move == "slash":
        damage = random.randint(1, 10)
    elif move == "stab":
        damage = random.randint(4, 6)
    elif move == "defend":
        damage = 0
        TensionPoints = TensionPoints + 10
        monster_damage=monster_damage/2
    elif move == "dodge":
        damage = 0
        monster_damage = 0
        TensionPoints = TensionPoints + 5
        chance2 = random.randint(1, 3)
        if chance2 == 2:
            print("You couldn't dodge in time!")
            monster_damage = 2
    elif move == "fireball":
        if TensionPoints < 20:
            print ("You do not have enough TP for that.")
        else:
            damage = random.randint(25, 30)
    elif move == "heal prayer":
        if TensionPoints < 15:
            print ("You do not have enough TP for that.")
        else:
            player_health = player_health + 8
            print ("You gained 8 health.")
    else:
        print ("That's not a valid move!\n")
        continue
    
    #Calculate damage dealt to the monster and subtract from health, also the damage the monster deals to you
    monster_health = monster_health-damage
    if monster_health <= 0:
        break
    player_health = player_health-monster_damage
    if monster_health < 0:
        monster_health = 0
    if player_health < 0:
        player_health = 0
    print(f"You've dealt {damage} damage! The monster now has {monster_health} health left.\n")
    print(f"The monster dealt {monster_damage} damage! You have {player_health} health left.")

#if you lose or win
if player_health == 0:
    print("You lost. Better luck next time...")
if monster_health == 0:
    print(f"You defeated {monster_name}!")
