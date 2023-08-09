import json
import random
number = random.randint(1, 2)
def save_game_state(filename, player_name, coins, stageprice, level, temp, wandermax):
    data = {
        "player_name": player_name,
        "coins": coins,
        "stageprice": stageprice,
        "level": level,
        "temp": temp,
        "wandermax": wandermax
    }
    with open(filename, "w") as file:
        json.dump(data, file)

def load_game_state(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def extract_key_value(json_data, key):
    try:
        data = json.loads(json_data)
        return data[key]
    except:
        return None

print("Welcome to Pokemon Light")
name = input("What is your name: ")
coins = 5
stageprice = 5
level = 5
temp = 0
wandermax = 0
xp = 0
potions = 5
xpneeded = 10
print("Welcome to the world of Pokemon")
input("Press Enter to continue...")
print("My name is Oak, but people call me the Pokemon Professor")
input("Press Enter to continue...")
print("This world is inhabited by creatures called Pokemon")
input("Press Enter to continue...")
print("For some people, Pokemon are pets, but for others, Pokemon are used to fight")
while True:
    rivalname = input("This Is Your Friend They Are Your Neighbor. What Is Their Name? ")
    yn = input("Your Friends Name Is " +rivalname+ "? Y/N ")
    if yn == "Y" or yn == "y":
        break
    else:
        continue

basepokechoice = ["Charmander", "charmander", "bulbasaur", "Bulbasaur", "squirtle", "Squirtle"]
baseenergyamount = 5

json_Charmander = '{"hp": 39, "maxhp": 282, "attack": 52, "maxattack": 223, "defence": 43, "maxdefence": 203, "special": "ember", "level": 5, "health": 39, "stage": 5, "type": "fire"}'
json_Bulbasaur = '{"hp": 32, "maxhp": 276, "attack": 50, "maxattack": 210, "defence": 41, "maxdefence": 203, "special": "vine whip", "level": 5, "health": 32, "stage": 5, "type": "grass"}'
json_Squirtle = '{"hp": 35, "maxhp": 273, "attack": 51, "maxattack": 220, "defence": 42, "maxdefence": 203, "special": "water cannon", "level": 5, "health": 35, "stage": 5, "type": "water"}'

while True:
    basepoke = input("Choose your first Pokemon (Charmander, Bulbasaur, Squirtle): ").lower()
    if basepoke in basepokechoice:
        if basepoke == "charmander" or basepoke == "Charmander":
            playerenergy = (f"Fire {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_Charmander)
        elif basepoke == "Bulbasaur" or basepoke == "bulbasaur":
            playerenergy = (f"Grass {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_Bulbasaur)
        elif basepoke == "Squirtle" or basepoke == "squirtle":
            playerenergy = (f"Water {baseenergyamount}").upper()
            pokemon_stats = json.loads(json_Squirtle)
        break
    else:
        print("Not an option, try again")
        continue
print("Your first Pokémon is:", basepoke.upper())
print("Player's energy:", playerenergy)
print("Pokemon stats:")
print("HP:", pokemon_stats["hp"])
print("Max HP:", pokemon_stats["maxhp"])
print("Attack:", pokemon_stats["attack"])
print("Max Attack:", pokemon_stats["maxattack"])
print("Defence:", pokemon_stats["defence"])
print("Max Defence:", pokemon_stats["maxdefence"])
print("Special:", pokemon_stats["special"])
print("Health:", pokemon_stats["health"])
print("Type:", pokemon_stats["type"])

choices = ["attack", "Attack", "Defend", "Heal", "Run", "defend", "heal", "run"]
rattatahealth = 60

firstfight = True
while True:
    print("You encounter a trainer with a Rattata equipped")
    if firstfight:
        print(f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}")
        firstfight = False

    while True:
        firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
        if firstattack == "attack" or firstattack == "Attack":
            print(f"You attacked Rattata and dealt {pokemon_stats['attack']} damage")
            rattatahealth -= pokemon_stats["attack"]
            print(f"Rattata now has {rattatahealth} health")
        elif firstattack == "defend" or firstattack == "Defend":
            print("You defended yourself against Rattata's attack that would have dealt 30 damage")
            print(f"You now have {pokemon_stats['health']} health")
        elif firstattack == "heal" or firstattack == "Heal":
            if potions > 0:
                pokemon_stats["health"] += 30
                potions -= 1
                print("Pokemon healed 30")
            else:
                print("You Dont Have Anymore Potions")
        elif firstattack == "run" or firstattack == "Run":
            print("You did not successfully run away")
        else:
            print("Not a valid input, it is now Rattatas turn")

        if rattatahealth <= 0:
            print("You defeated Rattata! Congratulations!")
            coins += 10
            xp += 10
            temp = 0
            break

        print("Now its Rattatas turn")
        if rattatahealth > 0:
            if number == 1:
                if firstattack == "defend" or firstattack == "Defend":
                    print("Rattata Attacked But You Defended")
                else:
                    pokemon_stats["health"] -= 30
                    print("Rattata attacked you and dealt 30 damage")
                    print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                    number = random.randint(1, 2)
            if number == 2:
                if rattatahealth < 40:
                    rattatahealth += 20
                    print("Rattata Has Healed")
                    print(f"Rattas health is now at {rattatahealth}")
                    number = random.randint(1, 2)
                else:
                    print("Rattata Tried To Heal But Was Already At Max Health")
                    number = random.randint(1, 2)

        if pokemon_stats["health"] <= 0:
            print("Your Pokemon fainted. You lost the battle.")
            coins -= 5
            temp += 1
            rattatahealth = 60
            pokemon_stats['health'] = pokemon_stats['hp']
            continue


    if temp == 0:
        print(f"Congratulations, You won your first battle and now have {coins} coins")
        rattatahealth = 60
    else:
        print(f"Sorry, you lost your first battle and now have {coins} coins")
        print("After You Heal Your Pokemon You Go And Face The Trainer Again")
        rattatahealth = 60
    
    if xp==xpneeded:
        print(f"Your {basepoke} Has Leveled Up")
        xp = xp - xpneeded
        xpneeded += 10
        if pokemon_stats['hp'] < pokemon_stats['maxhp']:
            pokemon_stats['hp'] += 10
        if pokemon_stats['attack'] < pokemon_stats['maxattack']:
            pokemon_stats['attack'] += 10
        if pokemon_stats['defence'] < pokemon_stats['maxdefence']:
            pokemon_stats['defence'] += 10
        pokemon_stats['health'] = pokemon_stats['hp']
        pokemon_stats['level'] += 1
        print(f"{basepoke} has been leveled up to level {pokemon_stats['level']}")
        print("Pokemon stats:")
        print("HP:", pokemon_stats["hp"])
        print("Max HP:", pokemon_stats["maxhp"])
        print("Attack:", pokemon_stats["attack"])
        print("Max Attack:", pokemon_stats["maxattack"])
        print("Defence:", pokemon_stats["defence"])
        print("Max Defence:", pokemon_stats["maxdefence"])
        print("Special:", pokemon_stats["special"])
        print("Health:", pokemon_stats["health"])
    while True:
        print(f"Ok {name}, you have proved yourself in the ability to train {basepoke}")
        input("Press Enter to continue...")
        print("Now you have the freedom to explore Kanto in its full beauty")
        input("Press Enter to continue...")
        print("You can type (1. for evolving your pokemon)")
        input("Press Enter to continue...")
        print("Press (2. To go to the arena and fight a pokemon)")
        input("Press Enter to continue...")
        print("Press (3. Wander around)")
        input("Press Enter to continue...")
        print("Press (4. To Explore The Shops)")
        input("Press Enter to continue...")
        print("Press (5. To check your stats)")
        input("Press Enter to continue...")
        print("Press (6. For help)")
        input("Press Enter to continue...")
        print("Press (7. To save and exit)")
        break
  
    while True:
        freechoice = input("What action do you want to perform? ")
        if freechoice == "1":
            if pokemon_stats['level'] >= 18:
                if basepoke == "charmander" or basepoke == "Charmander":
                    print("Your Charmander Has Evolved Into A Charmeleon")
                    basepoke = "Charmeleon"
                if basepoke == "Bulbasaur" or basepoke == "bulbasaur":
                    print("Your Bulbasaur Has Evolbed Into A Ivysaur")
                    basepoke = "Ivysaur"
                if basepoke == "Squirtle" or basepoke == "squirtle":
                    print("Your Squirtle Has Evolved Into A Warturtle")
                    basepoke = "Warturtle"
            if pokemon_stats['level'] >= 36:
                if basepoke == "charmander" or basepoke == "Charmander":
                    print("Your Charmander Has Evolved Into A Charmeleon And Then Evolved Into A Charzard")
                    basepoke = "Charzard"
                if basepoke == "Charmeleon":
                    print("Your Charmeleon Has Evolved Into A Charzard")
                    basepoke = "Charzard"
                if basepoke == "Bulbasaur" or basepoke == "bulbasaur":
                    print("Your Bulbasaur Has Evolved Into An Ivysaur and Then Evolved Into A Venusaur")
                    basepoke = "Venusaur"
                if basepoke == "Ivysaur":
                    print("Your Ivysaur Has Evolved Into A Venusaur")
                    basepoke = "Venusaur"
                if basepoke == "Squirtle" or basepoke == "squirtle":
                    print("Your Squirtle Has Evolved Into A Warturtle and Then Evolved Into A Blastoise")
                    basepoke = "Blastoise"
                if basepoke == "Warturtke":
                    print("Your Warturtle Has Evolved Into A Blastoise")
                    basepoke = "Blastoise"
            if pokemon_stats['level'] < 8 or basepoke == "Charzard" or basepoke == "Venusaur" or basepoke == "Blastoise":
                print("You Cannot Evolve")
        if freechoice == "2":

            pokemonchoicefree = ["tepig", "kyogre", "sneasler", "poliwhirl"]
            computerrandpoke = random.choice(pokemonchoicefree)
            tepighealth = 80
            tepigattack = 35
            kygorehealth = 130
            kygoreattack = 30
            sneaslerhealth = 120
            sneaslerattack = 30
            poliwhirlhealth = 90
            poliwhirlattack = 30
            print(f"You Go Into The Arena And A Trainer With A {computerrandpoke} Challenges You")
            if computerrandpoke == "tepig":
                while True:
                
                    firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                    if firstattack == "attack" or firstattack == "Attack":
                        print(f"You attacked tepig and dealt {pokemon_stats['attack']} damage")
                        tepighealth -= pokemon_stats["attack"]
                        print(f"tepig now has {tepighealth} health")
                    elif firstattack == "defend" or firstattack == "Defend":
                        print("You defended yourself against tepig's attack that would have dealt 35 damage")
                        print(f"You now have {pokemon_stats['health']} health")
                    elif firstattack == "heal" or firstattack == "Heal":
                        if potions > 0:
                            pokemon_stats["health"] += 30
                            potions -= 1
                            print("Pokemon healed 30")
                        else:
                            print("You Dont Have Anymore Potions")
                    elif firstattack == "run" or firstattack == "Run":
                        print("You did not successfully run away")
                    else:
                        print("Not a valid input, it is now tepigs turn")

                    if tepighealth <= 0:
                        print("You defeated tepig! Congratulations!")
                        coins += 10
                        xp += 10
                        temp = 0
                        break

                    print("Now its tepig's turn")
                    if tepighealth > 0:
                        if number == 1:
                            if firstattack == "defend" or firstattack == "Defend":
                                print("tepig Attacked But You Defended")
                            else:
                                pokemon_stats["health"] -= 35
                                print("Rattata attacked you and dealt 35 damage")
                                print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                                number = random.randint(1, 2)
                        if number == 2:
                            if tepighealth < 60:
                                tepighealth += 20
                                print("tepig Has Healed")
                                print(f"tepig health is now at {tepighealth}")
                                number = random.randint(1, 2)
                            else:
                                print("tepig Tried To Heal But Was Already At Max Health")
                                number = random.randint(1, 2)

                    if pokemon_stats["health"] <= 0:
                        print("Your Pokemon fainted. You lost the battle.")
                        coins -= 5
                        temp += 1
                        break
            if computerrandpoke == "kyogre":
                while True:
                
                    firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                    if firstattack == "attack" or firstattack == "Attack":
                        print(f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage")
                        kygorehealth -= pokemon_stats["attack"]
                        print(f"{computerrandpoke} now has {kygorehealth} health")
                    elif firstattack == "defend" or firstattack == "Defend":
                        print(f"You defended yourself against {computerrandpoke}'s attack that would have dealt {kygoreattack} damage")
                        print(f"You now have {pokemon_stats['health']} health")
                    elif firstattack == "heal" or firstattack == "Heal":
                        if potions > 0:
                            pokemon_stats["health"] += 30
                            potions -= 1
                            print("Pokemon healed 30")
                        else:
                            print("You Dont Have Anymore Potions")
                    elif firstattack == "run" or firstattack == "Run":
                        print("You did not successfully run away")
                    else:
                        print(f"Not a valid input, it is now {computerrandpoke}'s turn")

                    if kygorehealth <= 0:
                        print(f"You defeated {computerrandpoke}! Congratulations!")
                        coins += 10
                        xp += 40
                        temp = 0
                        break

                    print(f"Now its {computerrandpoke}'s turn")
                    if kygorehealth > 0:
                        if number == 1:
                            if firstattack == "defend" or firstattack == "Defend":
                                print("kogre Attacked But You Defended")
                            else:
                                pokemon_stats["health"] -= kygoreattack
                                print(f"{computerrandpoke} attacked you and dealt {kygoreattack} damage")
                                print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                                number = random.randint(1, 2)
                        if number == 2:
                            if kygorehealth < 110:
                                kygorehealth += 20
                                print(f"{computerrandpoke} Has Healed")
                                print(f"{computerrandpoke} health is now at {kygorehealth}")
                                number = random.randint(1, 2)
                            else:
                                print(f"{computerrandpoke} Tried To Heal But Was Already At Max Health")
                                number = random.randint(1, 2)

                    if pokemon_stats["health"] <= 0:
                        print("Your Pokemon fainted. You lost the battle.")
                        coins -= 5
                        temp += 1
                        break
            if computerrandpoke == "sneasler":
                while True:
                
                    firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                    if firstattack == "attack" or firstattack == "Attack":
                        print(f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage")
                        sneaslerhealth -= pokemon_stats["attack"]
                        print(f"{computerrandpoke} now has {sneaslerhealth} health")
                    elif firstattack == "defend" or firstattack == "Defend":
                        print(f"You defended yourself against {computerrandpoke}'s attack that would have dealt {sneaslerattack} damage")
                        print(f"You now have {pokemon_stats['health']} health")
                    elif firstattack == "heal" or firstattack == "Heal":
                        if potions > 0:
                            pokemon_stats["health"] += 30
                            potions -= 1
                            print("Pokemon healed 30")
                        else:
                            print("You Dont Have Anymore Potions")
                    elif firstattack == "run" or firstattack == "Run":
                        print("You did not successfully run away")
                    else:
                        print(f"Not a valid input, it is now {computerrandpoke}'s turn")

                    if sneaslerhealth <= 0:
                        print(f"You defeated {computerrandpoke}! Congratulations!")
                        coins += 10
                        xp += 20
                        temp = 0
                        break

                    print(f"Now its {computerrandpoke}'s turn")
                    if sneaslerhealth > 0:
                        if number == 1:
                            if firstattack == "defend" or firstattack == "Defend":
                                print(f"{computerrandpoke} Attacked But You Defended")
                            else:
                                pokemon_stats["health"] -= sneaslerattack
                                print(f"{computerrandpoke} attacked you and dealt {sneaslerattack} damage")
                                print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                                number = random.randint(1, 2)
                        if number == 2:
                            if sneaslerhealth < 100:
                                sneaslerhealth += 20
                                print(f"{computerrandpoke} Has Healed")
                                print(f"{computerrandpoke} health is now at {sneaslerhealth}")
                                number = random.randint(1, 2)
                            else:
                                print(f"{computerrandpoke} Tried To Heal But Was Already At Max Health")
                                number = random.randint(1, 2)

                    if pokemon_stats["health"] <= 0:
                        print("Your Pokemon fainted. You lost the battle.")
                        coins -= 5
                        temp += 1
                        break
            if computerrandpoke == "poliwhirl":
                while True:
                
                    firstattack = input("What is your move (Attack, Defend, Heal, Run): ").lower()
                    if firstattack == "attack" or firstattack == "Attack":
                        print(f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage")
                        poliwhirlhealth -= pokemon_stats["attack"]
                        print(f"{computerrandpoke} now has {poliwhirlhealth} health")
                    elif firstattack == "defend" or firstattack == "Defend":
                        print(f"You defended yourself against {computerrandpoke}'s attack that would have dealt {poliwhirlattack} damage")
                        print(f"You now have {pokemon_stats['health']} health")
                    elif firstattack == "heal" or firstattack == "Heal":
                        if potions > 0:
                            pokemon_stats["health"] += 30
                            potions -= 1
                            print("Pokemon healed 30")
                        else:
                            print("You Dont Have Anymore Potions")
                    elif firstattack == "run" or firstattack == "Run":
                        print("You did not successfully run away")
                    else:
                        print(f"Not a valid input, it is now {computerrandpoke}'s turn")

                    if poliwhirlhealth <= 0:
                        print(f"You defeated {computerrandpoke}! Congratulations!")
                        coins += 10
                        xp += 30
                        temp = 0
                        break

                    print(f"Now its {computerrandpoke}'s turn")
                    if poliwhirlhealth > 0:
                        if number == 1:
                            if firstattack == "defend" or firstattack == "Defend":
                                print(f"{computerrandpoke} Attacked But You Defended")
                            else:
                                pokemon_stats["health"] -= poliwhirlattack
                                print(f"{computerrandpoke} attacked you and dealt {sneaslerattack} damage")
                                print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                                number = random.randint(1, 2)
                        if number == 2:
                            if poliwhirlhealth < 70:
                                poliwhirlhealth += 20
                                print(f"{computerrandpoke} Has Healed")
                                print(f"{computerrandpoke} health is now at {poliwhirlhealth}")
                                number = random.randint(1, 2)
                            else:
                                print(f"{computerrandpoke} Tried To Heal But Was Already At Max Health")
                                number = random.randint(1, 2)

                    if pokemon_stats["health"] <= 0:
                        print("Your Pokemon fainted. You lost the battle.")
                        coins -= 5
                        temp += 1
                        break


            if temp == 0:
                print(f"Congratulations, You won your battle and now have {coins} coins")
                pokemon_stats["health"] = pokemon_stats['hp']
            else:
                print(f"Sorry, you lost your first battle and now have {coins} coins")
                pokemon_stats["health"] = pokemon_stats['hp']
            while xp==xpneeded:
                if xp==xpneeded:
                    print(f"Your {basepoke} Has Leveled Up")
                    xp = xp - xpneeded
                    xpneeded += 10
                    if pokemon_stats['hp'] < pokemon_stats['maxhp']:
                        pokemon_stats['hp'] += 10
                    if pokemon_stats['attack'] < pokemon_stats['maxattack']:
                        pokemon_stats['attack'] += 10
                    if pokemon_stats['defence'] < pokemon_stats['maxdefence']:
                        pokemon_stats['defence'] += 10
                    pokemon_stats['health'] = pokemon_stats['hp']
                    pokemon_stats['level'] += 1
                    print(f"{basepoke} has been leveled up to level {pokemon_stats['level']}")
                    print("Pokemon stats:")
                    print("HP:", pokemon_stats["hp"])
                    print("Max HP:", pokemon_stats["maxhp"])
                    print("Attack:", pokemon_stats["attack"])
                    print("Max Attack:", pokemon_stats["maxattack"])
                    print("Defence:", pokemon_stats["defence"])
                    print("Max Defence:", pokemon_stats["maxdefence"])
                    print("Special:", pokemon_stats["special"])
                    print("Health:", pokemon_stats["health"])
        if freechoice == "3":
            if wandermax <= 10:
              wanderingoptions = ["you found 5 coins on the ground", "you found a card for 7 energy", "you found a boost for 1 attack"]
              wanderoptions = random.choice(wanderingoptions)
              print(f"While wandering around {wanderoptions}")
              if wanderoptions == "you found 5 coins on the ground":
                coins += 5
                print(f"You have {coins} coins")
                wandermax += 1
              elif wanderoptions == "you found a card for 7 energy":
                baseenergyamount += 7
                print(f"You have {playerenergy} energy")
                wandermax += 1
              else:
                print(f"You have {pokemon_stats['attack']} attack")
                pokemon_stats['attack'] += 1
                wandermax += 1
            else:
              print("You Feel Tired And You Cant Wander Anymore")
              continue
        if freechoice == "4":
            choice4 = input("You walk into town and find 3 shops (Attack shop,  potoion shop,  Wander shop): ").lower()
            if choice4 == "attackshop" or choice4 == "attack shop":
              choice6 = input("Do you want to buy plus 10 attack for 100 coins (y/n)").lower()
              if choice6 == "y":
                if coins >= 100 and pokemon_stats["attack"] < pokemon_stats["maxattack"]:
                    pokemon_stats["attack"] += 10
                    coins -= 100
                    print(f"You have {pokemon_stats['attack']} attack")
                else:
                    print("You Cannot Afford This Or You Are Allready At Max Attack")
              elif choice6 == "n":
                print("Okay")
                continue
              else:
                print("Not an option")
                continue
            elif choice4 == "potionshop" or choice4 == "potion shop":
                choice8 = input(f"Do you want to spend 10 coins to buy 1 potion you have {coins} (y/n)")
                if choice8 == "y":
                    if coins >= 10:
                        potions += 1
                        coins -= 10
                        print(f"Okay, You have bought one potion you now have {potions} potion(s)")
                    else:
                        print("You Dont Have Enough Coins")
                elif choice8 == "n":
                    print("Okay")
                    continue
            elif choice4 == "wandershop" or choice4 == "wander shop":
                choice7 = input(f"Do you want to spend 50 coins to reset your wander count you have {coins} (y/n)").lower()
                if choice7 == "y":
                    if coins >= 50:
                        print("Okay, you now Can Wander Again")
                        coins -= 50
                        wandermax = 0
                        continue
                    else:
                        print("You Dont Have Enough Coins")
                        continue
                elif choice7 == "n":
                    print("Okay")
                    continue
                else:
                    print("Not an option")
                    continue
            else:
              print("Not an option")
              continue
        if freechoice == "5":
            print("Pokemon stats:")
            print("HP:", pokemon_stats["hp"])
            print("Max HP:", pokemon_stats["maxhp"])
            print("Attack:", pokemon_stats["attack"])
            print("Max Attack:", pokemon_stats["maxattack"])
            print("Defence:", pokemon_stats["defence"])
            print("Max Defence:", pokemon_stats["maxdefence"])
            print("Special:", pokemon_stats["special"])
            print("Health:", pokemon_stats["health"])
            print("Stage:", pokemon_stats["stage"])
            print(f"You have {coins} coins and {playerenergy} energy")

        if freechoice == "6":
            print("Now you have the freedom to explore Kanto in its full beauty")
            input("Press Enter to continue...")
            print("You can type (1. for upgrading your pokemon)")
            input("Press Enter to continue...")
            print("Press (2. To explore shops and equip your pokemon)")
            input("Press Enter to continue...")
            print("Press (3. To go to the arena and fight a pokemon)")
            input("Press Enter to continue...")
            print("Press (4. Wander around)")
            input("Press Enter to continue...")
            print("Press (5. To check your stats)")
            input("Press Enter to continue...")
            print("Press (6. For help)")
            input("Press Enter to continue...")
            print("Press (7. To save and exit)")
        if freechoice == "7":
            print("Bye")
            break
    break
print("Thanks for playing Pokemon Light!")
print(f"Your final stats: HP: {pokemon_stats['hp']}, Max HP: {pokemon_stats['maxhp']}, Attack: {pokemon_stats['attack']}, Max Attack: {pokemon_stats['maxattack']}, Defence: {pokemon_stats['defence']}, Max Defence: {pokemon_stats['maxdefence']}, Special: {pokemon_stats['special']}")
print("You collected", coins, "coins in total.")

        
