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
xpneeded = 10
while True:
    game = input("Do you want a new game or load saved game: ").lower()
    if game == "new game" or game == "newgame":
        print("Welcome to the world of Pokemon")
        input("Press Enter to continue...")
        print("My name is Oak, but people call me the Pokemon Professor")
        input("Press Enter to continue...")
        print("This world is inhabited by creatures called Pokemon")
        input("Press Enter to continue...")
        print("For some people, Pokemon are pets, but for others, Pokemon are used to fight")
        break
    elif game in ["load saved game", "savegame", "save game", "loadsavedgame", "load save game", "loadsavegame"]:
        save_file_name = f"{name.lower()}_save.json"
        saved_data = load_game_state(save_file_name)
        if saved_data:
            coins = saved_data.get("coins", coins)
            stageprice = saved_data.get("stageprice", stageprice)
            level = saved_data.get("level", level)
            temp = saved_data.get("temp", temp)
            wandermax = saved_data.get("wandermax", wandermax)
            print("Game loaded successfully!")
        else:
            print("No save game found. Starting a new game...")
        break
    else:
        print("Invalid input. Please choose 'new game' or 'load saved game'.")
        continue
while True:
    rivalname = input("This Is Your Friend. What Is Their Name? ")
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
                pokemon_stats["health"] += 30
                print("Pokemon healed 30")
        elif firstattack == "run" or firstattack == "Run":
            print("You did not successfully run away")
        else:
            print("Not a valid input, it is now Rattatas turn")

        if rattatahealth <= 0:
            print("You defeated Rattata! Congratulations!")
            coins += 10
            xp += 10
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

            break

    if temp == 0:
        print(f"Congratulations, You won your first battle and gained {coins} coins")
        rattatahealth = 60
    else:
        print(f"Sorry, you lost your first battle and now have {coins} coins")
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
        print("Press (4. To check your stats)")
        input("Press Enter to continue...")
        print("Press (5. For help)")
        input("Press Enter to continue...")
        print("Press (6. To save and exit)")
        break
  
    while True:
        freechoice = input("What action do you want to perform? ")
        if freechoice == "1":
            if pokemon_stats["level"] >= 18:
                if basepoke == "Charmander" or basepoke == "Charmander":
                    print("Your Charmander Has Evolved Into A Charmeleon")
                    basepoke = "Charmeleon"
                if basepoke == "Bulbasaur" or basepoke == "bulbasaur":
                    print("Your Bulbasaur Has Evolbed Into A Ivysaur")
                    basepoke = "Ivysaur"
                if basepoke == "Squirtle" or basepoke == "squirtle":
                    print("Your Squirtle Has Evolved Into A Warturtle")
                    basepoke = "Warturtle"
            elif pokemon_stats["level"] >= 36:
                if basepoke == "Charmander" or basepoke == "Charmander":
                    print("Your Charmander Has Evolved Into A Charmeleon And Then Evolved Into A Charzard")
                    basepoke = "Charzard"
                if basepoke == "Charmeleon":
                    print("Your Charmeleon Has Evolved Into A Charzard")
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
            else:
                print("You Cannot Evolve")
        if freechoice == "2":
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
                        pokemon_stats["health"] += 30
                        print("Pokemon healed 30")
                elif firstattack == "run" or firstattack == "Run":
                    print("You did not successfully run away")
                else:
                    print("Not a valid input, it is now Rattatas turn")

                if rattatahealth <= 0:
                    print("You defeated Rattata! Congratulations!")
                    coins += 10
                    xp += 10
                    rattatahealth = 60
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
                    break

            if temp == 0:
                print(f"Congratulations, You won your first battle and gained {coins} coins")
                rattatahealth = (60 * pokemon_stats["level"]) / 4
                pokemon_stats["health"] = pokemon_stats['hp']
            else:
                print(f"Sorry, you lost your first battle and now have {coins} coins")
                rattatahealth = (60 * pokemon_stats["level"]) / 4
                pokemon_stats["health"] = pokemon_stats['hp']

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
    break
        
