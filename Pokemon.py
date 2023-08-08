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
battlehealth = 
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
            print(f"Bulbasaur now has {rattatahealth} health")
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
            print("You defeated Bulbasaur! Congratulations!")
            coins += 10
            xp += 10
            break

        print("Now its Rattatas turn")
        if rattatahealth > 0:
            if number == 1:
                pokemon_stats["health"] -= 30
                print("Bulbasaur attacked you and dealt 30 damage")
                print(f"Your {basepoke} now has {pokemon_stats['health']} health")
                number = random.randint(1, 2)
            if number == 2:
                if rattatahealth < 40:
                    rattatahealth += 20
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
    else:
        print(f"Sorry, you lost your first battle and now have {coins} coins")
    
    if xp==xpneeded:
        print(f"Your {basepoke} Has Leveled Up")
        xp = xp - xpneeded
        xpneeded += 10
        pokemon_stats['hp'] += 10
        pokemon_stats['attack'] += 10
        pokemon_stats['defence'] += 10
        pokemon_stats['health'] == pokemon_stats['hp']
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



