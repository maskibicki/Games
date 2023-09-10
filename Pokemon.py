import json
import random
import time
from Classes.pokemon import Pokemon
from Classes.player import Player
from Classes.attack import Attack
from Classes.type import PokeType

number = random.randint(1, 2)

base_attack_data = []
base_pokemon_data = []
base_type_data = []

def load_game_data():
    global base_attack_data
    global base_pokemon_data
    global base_type_data

    print("load attacks")
    with open("data/all_attacks.json", "r") as file:
        base_attack_data = [Attack(**a) for a in json.load(file)]
    
    print("load pokemon")
    with open("data/all_pokemon.json", "r") as file:
        base_pokemon_data = [Pokemon(**p) for p in json.load(file)]
    
    print("load types")
    with open("data/all_types.json", "r") as file:
        base_type_data = [PokeType(**pt) for pt in json.load(file)]

def save_game_state(filename, player_name, coins, stageprice, level, temp,
                    wandermax):
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

load_game_data()

# print("There Is A Poll Avaliable For Voting On What Should Be Added Next. Go To https://forms.gle/hCS6tn3yFeqL2xD16. Loading Game...")
# time.sleep(10)
print("Welcome to Pokemon Light")
player = Player()
player.name = input("What is your name: ")
print("Welcome to the world of Pokemon")
input("Press Enter to continue...")
print("My name is Oak, but people call me the Pokemon Professor")
input("Press Enter to continue...")
print("This world is inhabited by creatures called Pokemon")
input("Press Enter to continue...")
print(
  "For some people, Pokemon are pets, but for others, Pokemon are used to fight"
)
while True:
  rivalname = input(
    "This Is Your Friend They Are Your Neighbor. What Is Their Name? ")
  yn = input("Your Friends Name Is " + rivalname + "? Y/N ")
  if yn == "Y" or yn == "y":
    break
  else:
    continue

basepokechoice = [
  "Charmander", "charmander", "bulbasaur", "Bulbasaur", "squirtle", "Squirtle"
]
baseenergyamount = 5

while True:
    starter_pokemon = [p.name for p in base_pokemon_data if p.starter_pokemon == True]  

    print("You can select one of these as your starter pokemon:")

    for pokemon in starter_pokemon: print(pokemon)

    basepoke = input("Choose One: ").lower()
    if basepoke in [sp.lower() for sp in starter_pokemon]:
        player.pokemon.append((next(p for p in base_pokemon_data if p.name.lower() == basepoke)))
        playerenergy = f"{player.pokemon[0].type} {baseenergyamount}"
        print(player)
        break
    else: 
        print("Not an option, try again")
        continue

print("Your first Pokémon is:", player.pokemon[0].name)
print("Player's energy:", playerenergy)
print("Pokemon stats:")
print("Current HP:", player.pokemon[0].current_hp)
print("Max HP:", player.pokemon[0].max_hp)
print("Attack:", player.pokemon[0].attack)
print("Special:", player.pokemon[0].attacks[0])
print("Type:", player.pokemon[0].type)

choices = [
  "attack", "Attack", "Defend", "Heal", "Run", "defend", "heal", "run"
]
rattatahealth = 60

firstfight = True
while True:
  while True:
    print("You encounter a trainer with a Rattata equipped")
    if firstfight:
      print(
        f"Your stats are HP: {pokemon_stats['health']}, Attack: {pokemon_stats['attack']}, Defence: {pokemon_stats['defence']}, Stage: {pokemon_stats['stage']}"
      )
      firstfight = False
  
    while True:
      firstattack = input(
        "What is your move (Attack, Defend, Heal, Run): ").lower()
      if firstattack == "attack" or firstattack == "Attack":
        print(f"You attacked Rattata and dealt {pokemon_stats['attack']} damage")
        rattatahealth -= pokemon_stats["attack"]
        print(f"Rattata now has {rattatahealth} health")
      elif firstattack == "defend" or firstattack == "Defend":
        print(
          "You defended yourself against Rattata's attack that would have dealt 30 damage"
        )
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
        totalcoins+=10
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
        break
  
    if temp == 0:
      print(
        f"Congratulations, You won your first battle and now have {coins} coins")
      rattatahealth = 60
      break
    else:
      print(f"Sorry, you lost your first battle and now have {coins} coins")
      print("After You Heal Your Pokemon You Go And Face The Trainer Again")
      rattatahealth = 60

  if xp == xpneeded:
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
    print(
      f"Ok {name}, you have proved yourself in the ability to train {basepoke}"
    )
    input("Press Enter to continue...")
    print("Now you have the freedom to explore Kanto in its full beauty")
    input("Press Enter to continue...")
    print("You can type (1. for evolving your pokemon)")
    input("Press Enter to continue...")
    print("Press (2. To go to the arena and fight a pokemon with only your starter pokemon)")
    input("Press Enter to continue...")
    print("Press (3. Wander around)")
    input("Press Enter to continue...")
    print("Press (4. To Explore The Shops)")
    input("Press Enter to continue...")
    print("Press (5. To check your stats)")
    input("Press Enter to continue...")
    print("Press (6. For help)")
    input("Press Enter to continue...")
    print("Press (7. To Catch Pokemon)")
    input("Press Enter To Continue...")
    print("Press (8. To Battle With Your Caught Pokemon)")
    input("Press Enter To Continue...")
    print("Press (9. To Get Rid Of Pokemon)")
    input("Press Enter To Contiue...")
    print("Press (10. To save and exit)")
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
          print(
            "Your Charmander Has Evolved Into A Charmeleon And Then Evolved Into A Charzard"
          )
          basepoke = "Charzard"
        if basepoke == "Charmeleon":
          print("Your Charmeleon Has Evolved Into A Charzard")
          basepoke = "Charzard"
        if basepoke == "Bulbasaur" or basepoke == "bulbasaur":
          print(
            "Your Bulbasaur Has Evolved Into An Ivysaur and Then Evolved Into A Venusaur"
          )
          basepoke = "Venusaur"
        if basepoke == "Ivysaur":
          print("Your Ivysaur Has Evolved Into A Venusaur")
          basepoke = "Venusaur"
        if basepoke == "Squirtle" or basepoke == "squirtle":
          print(
            "Your Squirtle Has Evolved Into A Warturtle and Then Evolved Into A Blastoise"
          )
          basepoke = "Blastoise"
        if basepoke == "Warturtle":
          print("Your Warturtle Has Evolved Into A Blastoise")
          basepoke = "Blastoise"
      if pokemon_stats[
          'level'] < 18 or basepoke == "Charzard" or basepoke == "Venusaur" or basepoke == "Blastoise":
        print("You Cannot Evolve")
    if freechoice == "2":

      pokemonchoicefree = ["tepig", "kyogre", "sneasler", "poliwhirl"]
      computerrandpoke = random.choice(pokemonchoicefree)
      tepighealth = (80 * pokemon_stats["level"]) / 6
      tepigattack = (35 * pokemon_stats["level"]) / 10
      kygorehealth = (130 * pokemon_stats["level"]) / 6
      kygoreattack = (30 * pokemon_stats["level"]) / 10
      sneaslerhealth = (120 * pokemon_stats["level"]) / 6
      sneaslerattack = (30 * pokemon_stats["level"]) / 10
      poliwhirlhealth = (90 * pokemon_stats["level"]) / 6
      poliwhirlattack = (30 * pokemon_stats["level"]) / 10
      print(
        f"You Go Into The Arena And A Trainer With A {computerrandpoke} Challenges You"
      )
      if computerrandpoke == "tepig":
        while True:

          firstattack = input(
            "What is your move (Attack, Defend, Heal, Run): ").lower()
          if firstattack == "attack" or firstattack == "Attack":
            print(
              f"You attacked tepig and dealt {pokemon_stats['attack']} damage")
            tepighealth -= pokemon_stats["attack"]
            print(f"tepig now has {tepighealth} health")
          elif firstattack == "defend" or firstattack == "Defend":
            print(
              "You defended yourself against tepig's attack that would have dealt 35 damage"
            )
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
            totalcoins+=10
            xp += (10 * pokemon_stats["level"]) / 2
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
                print(
                  f"Your {basepoke} now has {pokemon_stats['health']} health")
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

          firstattack = input(
            "What is your move (Attack, Defend, Heal, Run): ").lower()
          if firstattack == "attack" or firstattack == "Attack":
            print(
              f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage"
            )
            kygorehealth -= pokemon_stats["attack"]
            print(f"{computerrandpoke} now has {kygorehealth} health")
          elif firstattack == "defend" or firstattack == "Defend":
            print(
              f"You defended yourself against {computerrandpoke}'s attack that would have dealt {kygoreattack} damage"
            )
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
            totalcoins+=10
            xp += (40 * pokemon_stats["level"]) / 6
            temp = 0
            break

          print(f"Now its {computerrandpoke}'s turn")
          if kygorehealth > 0:
            if number == 1:
              if firstattack == "defend" or firstattack == "Defend":
                print("kogre Attacked But You Defended")
              else:
                pokemon_stats["health"] -= kygoreattack
                print(
                  f"{computerrandpoke} attacked you and dealt {kygoreattack} damage"
                )
                print(
                  f"Your {basepoke} now has {pokemon_stats['health']} health")
                number = random.randint(1, 2)
            if number == 2:
              if kygorehealth < 110:
                kygorehealth += 20
                print(f"{computerrandpoke} Has Healed")
                print(f"{computerrandpoke} health is now at {kygorehealth}")
                number = random.randint(1, 2)
              else:
                print(
                  f"{computerrandpoke} Tried To Heal But Was Already At Max Health"
                )
                number = random.randint(1, 2)

          if pokemon_stats["health"] <= 0:
            print("Your Pokemon fainted. You lost the battle.")
            coins -= 5
            temp += 1
            break
      if computerrandpoke == "sneasler":
        while True:

          firstattack = input(
            "What is your move (Attack, Defend, Heal, Run): ").lower()
          if firstattack == "attack" or firstattack == "Attack":
            print(
              f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage"
            )
            sneaslerhealth -= pokemon_stats["attack"]
            print(f"{computerrandpoke} now has {sneaslerhealth} health")
          elif firstattack == "defend" or firstattack == "Defend":
            print(
              f"You defended yourself against {computerrandpoke}'s attack that would have dealt {sneaslerattack} damage"
            )
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
            totalcoins+=10
            xp += (20 * pokemon_stats["level"]) / 3
            temp = 0
            break

          print(f"Now its {computerrandpoke}'s turn")
          if sneaslerhealth > 0:
            if number == 1:
              if firstattack == "defend" or firstattack == "Defend":
                print(f"{computerrandpoke} Attacked But You Defended")
              else:
                pokemon_stats["health"] -= sneaslerattack
                print(
                  f"{computerrandpoke} attacked you and dealt {sneaslerattack} damage"
                )
                print(
                  f"Your {basepoke} now has {pokemon_stats['health']} health")
                number = random.randint(1, 2)
            if number == 2:
              if sneaslerhealth < 100:
                sneaslerhealth += 20
                print(f"{computerrandpoke} Has Healed")
                print(f"{computerrandpoke} health is now at {sneaslerhealth}")
                number = random.randint(1, 2)
              else:
                print(
                  f"{computerrandpoke} Tried To Heal But Was Already At Max Health"
                )
                number = random.randint(1, 2)

          if pokemon_stats["health"] <= 0:
            print("Your Pokemon fainted. You lost the battle.")
            coins -= 5
            temp += 1
            break
      if computerrandpoke == "poliwhirl":
        while True:

          firstattack = input(
            "What is your move (Attack, Defend, Heal, Run): ").lower()
          if firstattack == "attack" or firstattack == "Attack":
            print(
              f"You attacked {computerrandpoke} and dealt {pokemon_stats['attack']} damage"
            )
            poliwhirlhealth -= pokemon_stats["attack"]
            print(f"{computerrandpoke} now has {poliwhirlhealth} health")
          elif firstattack == "defend" or firstattack == "Defend":
            print(
              f"You defended yourself against {computerrandpoke}'s attack that would have dealt {poliwhirlattack} damage"
            )
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
            totalcoins+=10
            xp += (30 * pokemon_stats["level"]) / 5
            temp = 0
            break

          print(f"Now its {computerrandpoke}'s turn")
          if poliwhirlhealth > 0:
            if number == 1:
              if firstattack == "defend" or firstattack == "Defend":
                print(f"{computerrandpoke} Attacked But You Defended")
              else:
                pokemon_stats["health"] -= poliwhirlattack
                print(
                  f"{computerrandpoke} attacked you and dealt {sneaslerattack} damage"
                )
                print(
                  f"Your {basepoke} now has {pokemon_stats['health']} health")
                number = random.randint(1, 2)
            if number == 2:
              if poliwhirlhealth < 70:
                poliwhirlhealth += 20
                print(f"{computerrandpoke} Has Healed")
                print(f"{computerrandpoke} health is now at {poliwhirlhealth}")
                number = random.randint(1, 2)
              else:
                print(
                  f"{computerrandpoke} Tried To Heal But Was Already At Max Health"
                )
                number = random.randint(1, 2)

          if pokemon_stats["health"] <= 0:
            print("Your Pokemon fainted. You lost the battle.")
            coins -= 5
            temp += 1
            break

      if temp == 0:
        print(
          f"Congratulations, You won your battle and now have {coins} coins")
        pokemon_stats["health"] = pokemon_stats['hp']
      else:
        print(f"Sorry, you lost your first battle and now have {coins} coins")
        pokemon_stats["health"] = pokemon_stats['hp']
      while xp >= xpneeded:
        if xp >= xpneeded:
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
          print(
            f"{basepoke} has been leveled up to level {pokemon_stats['level']}"
          )
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
        wanderingoptions = [
          "you found 5 coins on the ground", "you found a boost for 1 health",
          "you found a boost for 1 attack"
        ]
        wanderoptions = random.choice(wanderingoptions)
        print(f"While wandering around {wanderoptions}")
        if wanderoptions == "you found 5 coins on the ground":
          coins += 5
          totalcoins+=5
          print(f"You have {coins} coins")
          wandermax += 1
        elif wanderoptions == "you found a boost for 1 health":
          if pokemon_stats['hp'] < pokemon_stats['maxhp']:
            pokemon_stats['hp'] += 1
            pokemon_stats['health'] += 1
            print(f"You have {pokemon_stats['hp']} hp")
          wandermax += 1
          if pokemon_stats['hp'] >= pokemon_stats['maxhp']:
              print("You Are At Max Hp So You Dont Get A Boost (This Will Not Count For One Of Your Wanders")          
        else:
          if pokemon_stats['attack'] < pokemon_stats['maxattack']:
            pokemon_stats['attack'] += 1
            print(f"You have {pokemon_stats['attack']} attack")
          wandermax += 1
          if pokemon_stats['attack'] >= pokemon_stats['maxattack']:
              print("You Are At Max Attack So You Dont Get A Boost (This Will Not Count For One Of Your Wanders")  
      else:
        print("You Feel Tired And You Cant Wander Anymore")
        continue
    if freechoice == "4":
      choice4 = input(
        "You walk into town and find 4 shops (Attack shop,  potoion shop,  Wander shop, Pokeball Shop): "
      ).lower()
      if choice4 == "attackshop" or choice4 == "attack shop":
        choice6 = input(
          "Do you want to buy plus 10 attack for 100 coins (y/n)").lower()
        if choice6 == "y":
          if coins >= 100 and pokemon_stats["attack"] < pokemon_stats[
              "maxattack"]:
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
        choice8 = input(
          f"Do you want to spend 10 coins to buy 1 potion you have {coins} (y/n)"
        )
        if choice8 == "y":
          if coins >= 10:
            potions += 1
            coins -= 10
            print(
              f"Okay, You have bought one potion you now have {potions} potion(s)"
            )
          else:
            print("You Dont Have Enough Coins")
        elif choice8 == "n":
          print("Okay")
          continue
      elif choice4 == "wandershop" or choice4 == "wander shop":
        choice7 = input(
          f"Do you want to spend 50 coins to reset your wander count you have {coins} (y/n)"
        ).lower()
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
      elif choice4 == "pokeball shop" or choice4 == "Pokeball Shop":
        choice7 = input(
          f"Do you want to spend 10 coins to buy 5 more pokeballs you have {coins} (y/n) "
        ).lower()
        if choice7 == "y":
          if coins >= 10:
            pokeballs += 5
            print(f"Okay, you now have {pokeballs}")
            coins -= 10
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
      print(f"You have {coins} coins")

    if freechoice == "6":
      print("You can type (1. for evolving your pokemon)")
      input("Press Enter to continue...")
      print("Press (2. To go to the arena and fight a pokemon with only your starter pokemon)")
      input("Press Enter to continue...")
      print("Press (3. Wander around)")
      input("Press Enter to continue...")
      print("Press (4. To Explore The Shops)")
      input("Press Enter to continue...")
      print("Press (5. To check your stats)")
      input("Press Enter to continue...")
      print("Press (6. For help)")
      input("Press Enter to continue...")
      print("Press (7. To Catch Pokemon)")
      input("Press Enter To Continue...")
      print("Press (8. To Battle With Your Caught Pokemon)")
      input("Press Enter To Continue...")
      print("Press (9. To Get Rid Of Pokemon)")
      input("Press Enter To Contiue...")
      print("Press (10. To save and exit)")
    if freechoice == "7":


      catchpoke = ["Rattata", "Psyduck", "Pidove"]
      json_Rattata = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "scratch", "level": 5, "health": 55, "stage": 5, "type": "normal", "name": "rattata"}'
      json_Psyduck = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "psybeam", "level": 5, "health": 55, "stage": 5, "type": "water", "name": "pysduck"}'
      json_Pidove = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "peck", "level": 5, "health": 55, "stage": 5, "type": "flying", "name": "pidove"}'
      json_Rattata1 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "scratch", "level": 5, "health": 55, "stage": 5, "type": "normal", "name": "rattata"}'
      json_Psyduck1 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "psybeam", "level": 5, "health": 55, "stage": 5, "type": "water", "name": "pysduck"}'
      json_Pidove1 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "peck", "level": 5, "health": 55, "stage": 5, "type": "flying", "name": "pidove"}'
      json_Rattata2 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "scratch", "level": 5, "health": 55, "stage": 5, "type": "normal", "name": "rattata"}'
      json_Psyduck2 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "psybeam", "level": 5, "health": 55, "stage": 5, "type": "water", "name": "pysduck"}'
      json_Pidove2 = '{"hp": 55, "maxhp": 300, "attack": 52, "maxattack": 300, "defence": 55, "maxdefence": 300, "special": "peck", "level": 5, "health": 55, "stage": 5, "type": "flying", "name": "pidove"}'

      if second == "None":
        catch = random.choice(catchpoke)
        if catch == "Rattata":
          print("You Encountered A Wild Rattata")
        if catch == "Psyduck":
          print("You Encountered A Wild Pysduck")
        if catch == "Pidove":
          print("You Encountered A Wild Pidove")
        while True:
          if pokeballs > 0:
            ifcatch = input("Do You Want To Throw A Pokeball (Y/N) ")
            if ifcatch =="Y" or ifcatch == "y" or ifcatch == "Yes" or ifcatch == "yes":
              catchtry = random.randint(1, 2)
              print("You Throw A Pokeball")
              if catchtry == 1:
                print(f"You Caught {catch}!")
                pokeballs -= 1
                if catch == "Rattata":
                  secondpokemon_stats = json.loads(json_Rattata)
                  print("Pokemon stats:")
                  print("HP:", secondpokemon_stats["hp"])
                  print("Max HP:", secondpokemon_stats["maxhp"])
                  print("Attack:", secondpokemon_stats["attack"])
                  print("Max Attack:", secondpokemon_stats["maxattack"])
                  print("Defence:", secondpokemon_stats["defence"])
                  print("Max Defence:", secondpokemon_stats["maxdefence"])
                  print("Special:", secondpokemon_stats["special"])
                  print("Health:", secondpokemon_stats["health"])
                  print("Type:", secondpokemon_stats["type"])
                  second = "Rattata"
                if catch == "Pysduck":
                  secondpokemon_stats = json.loads(json_Psyduck)
                  second = "Pysduck"
                  print("Pokemon stats:")
                  print("HP:", secondpokemon_stats["hp"])
                  print("Max HP:", secondpokemon_stats["maxhp"])
                  print("Attack:", secondpokemon_stats["attack"])
                  print("Max Attack:", secondpokemon_stats["maxattack"])
                  print("Defence:", secondpokemon_stats["defence"])
                  print("Max Defence:", secondpokemon_stats["maxdefence"])
                  print("Special:", secondpokemon_stats["special"])
                  print("Health:", secondpokemon_stats["health"])
                  print("Type:", secondpokemon_stats["type"])
                if catch == "Pidove":
                  secondpokemon_stats = json.loads(json_Pidove)
                  second = "Pidove"
                  print("Pokemon stats:")
                  print("HP:", secondpokemon_stats["hp"])
                  print("Max HP:", secondpokemon_stats["maxhp"])
                  print("Attack:", secondpokemon_stats["attack"])
                  print("Max Attack:", secondpokemon_stats["maxattack"])
                  print("Defence:", secondpokemon_stats["defence"])
                  print("Max Defence:", secondpokemon_stats["maxdefence"])
                  print("Special:", secondpokemon_stats["special"])
                  print("Health:", secondpokemon_stats["health"])
                  print("Type:", secondpokemon_stats["type"])
                
                break
              if catchtry == 2:
                pokeballs -= 1
                print(f"Oh No! {catch} Broke Out")
                continue
            if ifcatch =="N" or ifcatch == "n" or ifcatch == "No" or ifcatch == "no":
              print("You Ran Away")
              break
          else:
            print("You Have No Pokeballs")
            break
      if third == "None":
        catch = random.choice(catchpoke)
        if catch == "Rattata":
          print("You Encountered A Wild Rattata")
        if catch == "Psyduck":
          print("You Encountered A Wild Pysduck")
        if catch == "Pidove":
          print("You Encountered A Wild Pidove")
        while True:
          if pokeballs > 0:
            ifcatch = input("Do You Want To Throw A Pokeball (Y/N)")
            if ifcatch =="Y" or ifcatch == "y" or ifcatch == "Yes" or ifcatch == "yes":
              catchtry = random.randint(1, 2)
              print("You Throw A Pokeball")
              if catchtry == 1:
                print(f"You Caught {catch}!")
                pokeballs -= 1
                if catch == "Rattata":
                  thirdpokemon_stats = json.loads(json_Rattata1)
                  third = "Rattata"
                  print("Pokemon stats:")
                  print("HP:", thirdpokemon_stats["hp"])
                  print("Max HP:", thirdpokemon_stats["maxhp"])
                  print("Attack:", thirdpokemon_stats["attack"])
                  print("Max Attack:", thirdpokemon_stats["maxattack"])
                  print("Defence:", thirdpokemon_stats["defence"])
                  print("Max Defence:", thirdpokemon_stats["maxdefence"])
                  print("Special:", thirdpokemon_stats["special"])
                  print("Health:", thirdpokemon_stats["health"])
                  print("Type:", thirdpokemon_stats["type"])
                if catch == "Pysduck":
                  thirdpokemon_stats = json.loads(json_Psyduck1)
                  third = "Pysduck"
                  print("Pokemon stats:")
                  print("HP:", thirdpokemon_stats["hp"])
                  print("Max HP:", thirdpokemon_stats["maxhp"])
                  print("Attack:", thirdpokemon_stats["attack"])
                  print("Max Attack:", thirdpokemon_stats["maxattack"])
                  print("Defence:", thirdpokemon_stats["defence"])
                  print("Max Defence:", thirdpokemon_stats["maxdefence"])
                  print("Special:", thirdpokemon_stats["special"])
                  print("Health:", thirdpokemon_stats["health"])
                  print("Type:", thirdpokemon_stats["type"])
                if catch == "Pidove":
                  thirdpokemon_stats = json.loads(json_Pidove1)
                  third = "Pidove"
                  print("Pokemon stats:")
                  print("HP:", thirdpokemon_stats["hp"])
                  print("Max HP:", thirdpokemon_stats["maxhp"])
                  print("Attack:", thirdpokemon_stats["attack"])
                  print("Max Attack:", thirdpokemon_stats["maxattack"])
                  print("Defence:", thirdpokemon_stats["defence"])
                  print("Max Defence:", thirdpokemon_stats["maxdefence"])
                  print("Special:", thirdpokemon_stats["special"])
                  print("Health:", thirdpokemon_stats["health"])
                  print("Type:", thirdpokemon_stats["type"])
                break
              if catchtry == 2:
                pokeballs -= 1
                print(f"Oh No! {catch} Broke Out")
                continue
            if ifcatch =="N" or ifcatch == "n" or ifcatch == "No" or ifcatch == "no":
              print("You Ran Away")
              break
          else:
            print("You Have No Pokeballs")
            break
      if fourth == "None":
        catch = random.choice(catchpoke)
        if catch == "Rattata":
          print("You Encountered A Wild Rattata")
        if catch == "Psyduck":
          print("You Encountered A Wild Pysduck")
        if catch == "Pidove":
          print("You Encountered A Wild Pidove")
        while True:
          if pokeballs > 0:
            ifcatch = input("Do You Want To Throw A Pokeball (Y/N)")
            if ifcatch =="Y" or ifcatch == "y" or ifcatch == "Yes" or ifcatch == "yes":
              catchtry = random.randint(1, 2)
              print("You Throw A Pokeball")
              if catchtry == 1:
                print(f"You Caught {catch}!")
                pokeballs -= 1
                if catch == "Rattata":
                  fourthpokemon_stats = json.loads(json_Rattata2)
                  fourth = "Rattata"
                  print("Pokemon stats:")
                  print("HP:", fourthpokemon_stats["hp"])
                  print("Max HP:", fourthpokemon_stats["maxhp"])
                  print("Attack:", fourthpokemon_stats["attack"])
                  print("Max Attack:", fourthpokemon_stats["maxattack"])
                  print("Defence:", fourthpokemon_stats["defence"])
                  print("Max Defence:", fourthpokemon_stats["maxdefence"])
                  print("Special:", fourthpokemon_stats["special"])
                  print("Health:", fourthpokemon_stats["health"])
                  print("Type:", fourthpokemon_stats["type"])
                if catch == "Pysduck":
                  fourthpokemon_stats = json.loads(json_Psyduck2)
                  fourth = "Pysduck"
                  print("Pokemon stats:")
                  print("HP:", fourthpokemon_stats["hp"])
                  print("Max HP:", fourthpokemon_stats["maxhp"])
                  print("Attack:", fourthpokemon_stats["attack"])
                  print("Max Attack:", fourthpokemon_stats["maxattack"])
                  print("Defence:", fourthpokemon_stats["defence"])
                  print("Max Defence:", fourthpokemon_stats["maxdefence"])
                  print("Special:", fourthpokemon_stats["special"])
                  print("Health:", fourthpokemon_stats["health"])
                  print("Type:", fourthpokemon_stats["type"])
                if catch == "Pidove":
                  fourthpokemon_stats = json.loads(json_Pidove2)
                  fourth = "Pidove"
                  print("Pokemon stats:")
                  print("HP:", fourthpokemon_stats["hp"])
                  print("Max HP:", fourthpokemon_stats["maxhp"])
                  print("Attack:", fourthpokemon_stats["attack"])
                  print("Max Attack:", fourthpokemon_stats["maxattack"])
                  print("Defence:", fourthpokemon_stats["defence"])
                  print("Max Defence:", fourthpokemon_stats["maxdefence"])
                  print("Special:", fourthpokemon_stats["special"])
                  print("Health:", fourthpokemon_stats["health"])
                  print("Type:", fourthpokemon_stats["type"])
                break
              if catchtry == 2:
                pokeballs -= 1
                print(f"Oh No! {catch} Broke Out")
                continue
            if ifcatch =="N" or ifcatch == "n" or ifcatch == "No" or ifcatch == "no":
              print("You Ran Away")
              break
          else:
            print("You Have No Pokeballs")
            break
      if second != "None" and third != "None" and fourth != "None":
        print("You Cant Catch Another Pokemon")
    if freechoice == "8":
      whichpoke = input("Which Pokemon Do You Want To Use? First, Second Or Third? (Enter 1, 2, 3 or 4) ")
      
      if whichpoke == "1":
        tepighealth = (80 * pokemon_stats["level"]) / 6
        tepigattack = (35 * pokemon_stats["level"]) / 10
        while True:

          firstattack = input(
            "What is your move (Attack, Defend, Heal, Run): ").lower()
          if firstattack == "attack" or firstattack == "Attack":
            print(
              f"You attacked tepig and dealt {pokemon_stats['attack']} damage")
            tepighealth -= pokemon_stats["attack"]
            print(f"tepig now has {tepighealth} health")
          elif firstattack == "defend" or firstattack == "Defend":
            print(
              "You defended yourself against tepig's attack that would have dealt 35 damage"
            )
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
            totalcoins +=10
            xp += (10 * pokemon_stats["level"]) / 2
            temp = 0
            break

          print("Now its tepig's turn")
          if tepighealth > 0:
            if number == 1:
              if firstattack == "defend" or firstattack == "Defend":
                print("tepig Attacked But You Defended")
              else:
                pokemon_stats["health"] -= 35
                print("Tepig attacked you and dealt 35 damage")
                print(
                  f"Your {basepoke} now has {pokemon_stats['health']} health")
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
      if whichpoke == "2":
        if second == "None":
          print("You Dont Have A Second Pokemon")
        else:
          tepighealth = (80 * secondpokemon_stats["level"]) / 6
          tepigattack = (35 * secondpokemon_stats["level"]) / 10
          while True:
  
            firstattack = input(
              "What is your move (Attack, Defend, Heal, Run): ").lower()
            if firstattack == "attack" or firstattack == "Attack":
              print(
                f"You attacked tepig and dealt {secondpokemon_stats['attack']} damage")
              tepighealth -= secondpokemon_stats["attack"]
              print(f"tepig now has {tepighealth} health")
            elif firstattack == "defend" or firstattack == "Defend":
              print(
                "You defended yourself against tepig's attack that would have dealt 35 damage"
              )
              print(f"You now have {secondpokemon_stats['health']} health")
            elif firstattack == "heal" or firstattack == "Heal":
              if potions > 0:
                secondpokemon_stats["health"] += 30
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
              totalcoins +=10
              secondxp += (10 * secondpokemon_stats["level"]) / 2
              temp = 0
              break
  
            print("Now its tepig's turn")
            if tepighealth > 0:
              if number == 1:
                if firstattack == "defend" or firstattack == "Defend":
                  print("tepig Attacked But You Defended")
                else:
                  secondpokemon_stats["health"] -= 35
                  print("Tepig attacked you and dealt 35 damage")
                  print(
                    f"Your {second} now has {secondpokemon_stats['health']} health")
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
  
            if secondpokemon_stats["health"] <= 0:
              print("Your Pokemon fainted. You lost the battle.")
              coins -= 5
              temp += 1
              break

      if whichpoke == "3":
        if third == "None":
          print("You dont have a third pokemon")
        else:
          tepighealth = (80 * thirdpokemon_stats["level"]) / 6
          tepigattack = (35 * thirdpokemon_stats["level"]) / 10
          while True:
  
            firstattack = input(
              "What is your move (Attack, Defend, Heal, Run): ").lower()
            if firstattack == "attack" or firstattack == "Attack":
              print(
                f"You attacked tepig and dealt {thirdpokemon_stats['attack']} damage")
              tepighealth -= thirdpokemon_stats["attack"]
              print(f"tepig now has {tepighealth} health")
            elif firstattack == "defend" or firstattack == "Defend":
              print(
                "You defended yourself against tepig's attack that would have dealt 35 damage"
              )
              print(f"You now have {thirdpokemon_stats['health']} health")
            elif firstattack == "heal" or firstattack == "Heal":
              if potions > 0:
                thirdpokemon_stats["health"] += 30
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
              totalcoins += 10
              thirdxp += (10 * thirdpokemon_stats["level"]) / 2
              temp = 0
              break
  
            print("Now its tepig's turn")
            if tepighealth > 0:
              if number == 1:
                if firstattack == "defend" or firstattack == "Defend":
                  print("tepig Attacked But You Defended")
                else:
                  thirdpokemon_stats["health"] -= 35
                  print("Tepig attacked you and dealt 35 damage")
                  print(
                    f"Your {third} now has {thirdpokemon_stats['health']} health")
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
  
            if thirdpokemon_stats["health"] <= 0:
              print("Your Pokemon fainted. You lost the battle.")
              coins -= 5
              temp += 1
              break
      if whichpoke == "4":
        if fourth == "None":
          print("You dont have a fourth pokemon")
        else:
          tepighealth = (80 * fourthpokemon_stats["level"]) / 6
          tepigattack = (35 * fourthpokemon_stats["level"]) / 10
          while True:
  
            firstattack = input(
              "What is your move (Attack, Defend, Heal, Run): ").lower()
            if firstattack == "attack" or firstattack == "Attack":
              print(
                f"You attacked tepig and dealt {fourthpokemon_stats['attack']} damage")
              tepighealth -= fourthpokemon_stats["attack"]
              print(f"tepig now has {tepighealth} health")
            elif firstattack == "defend" or firstattack == "Defend":
              print(
                "You defended yourself against tepig's attack that would have dealt 35 damage"
              )
              print(f"You now have {fourthpokemon_stats['health']} health")
            elif firstattack == "heal" or firstattack == "Heal":
              if potions > 0:
                fourthpokemon_stats["health"] += 30
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
              totalcoins += 10
              fourthxp += (10 * fourthpokemon_stats["level"]) / 2
              temp = 0
              break
  
            print("Now its tepig's turn")
            if tepighealth > 0:
              if number == 1:
                if firstattack == "defend" or firstattack == "Defend":
                  print("tepig Attacked But You Defended")
                else:
                  fouthpokemon_stats["health"] -= 35
                  print("Tepig attacked you and dealt 35 damage")
                  print(
                    f"Your {fourth} now has {fourthpokemon_stats['health']} health")
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
  
            if fourthpokemon_stats["health"] <= 0:
              print("Your Pokemon fainted. You lost the battle.")
              coins -= 5
              temp += 1
              break
      while xp >= xpneeded:
        if xp >= xpneeded:
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
      while secondxp >= secondxpneeded:
        if secondxp >= secondxpneeded:
          print(f"Your {second} Has Leveled Up")
          secondxp = secondxp - secondxpneeded
          secondxpneeded += 10
          if secondpokemon_stats['hp'] < secondpokemon_stats['maxhp']:
            secondpokemon_stats['hp'] += 10
          if secondpokemon_stats['attack'] < secondpokemon_stats['maxattack']:
            secondpokemon_stats['attack'] += 10
          if secondpokemon_stats['defence'] < secondpokemon_stats['maxdefence']:
            secondpokemon_stats['defence'] += 10
          secondpokemon_stats['health'] = secondpokemon_stats['hp']
          secondpokemon_stats['level'] += 1
          print(f"{second} has been leveled up to level {secondpokemon_stats['level']}")
      while thirdxp >= thirdxpneeded:
        if thirdxp >= thirdxpneeded:
          print(f"Your {third} Has Leveled Up")
          thirdxp = thirdxp - thirdxpneeded
          thirdxpneeded += 10
          if thirdpokemon_stats['hp'] < thirdpokemon_stats['maxhp']:
            thirdpokemon_stats['hp'] += 10
          if thirdpokemon_stats['attack'] < thirdpokemon_stats['maxattack']:
            thirdpokemon_stats['attack'] += 10
          if thirdpokemon_stats['defence'] < thirdpokemon_stats['maxdefence']:
            thirdpokemon_stats['defence'] += 10
          thirdpokemon_stats['health'] = thirdpokemon_stats['hp']
          thirdpokemon_stats['level'] += 1
          print(f"{third} has been leveled up to level {thirdpokemon_stats['level']}")
      while fourthxp >= fourthxpneeded:
        if fourthxp >= fourthxpneeded:
          print(f"Your {fourth} Has Leveled Up")
          fourthxp = fourthxp - fourthxpneeded
          fourthxpneeded += 10
          if fourthpokemon_stats['hp'] < fourthpokemon_stats['maxhp']:
            fourthpokemon_stats['hp'] += 10
          if fourthpokemon_stats['attack'] < fourthpokemon_stats['maxattack']:
            fourthpokemon_stats['attack'] += 10
          if fourthpokemon_stats['defence'] < fourthpokemon_stats['maxdefence']:
            fourthpokemon_stats['defence'] += 10
          fourthpokemon_stats['health'] = fourthpokemon_stats['hp']
          fourthpokemon_stats['level'] += 1
          print(f"{fourth} has been leveled up to level {fourthpokemon_stats['level']}")

    if freechoice =="9":
      rid = input("What Pokemon Do You Want To Get Rid Of? (Type 2 or 3) ")
      if rid =="2":
        second = "None"
        print("You Got Rid Of Your Second Pokemon")
        if secondpokemon_stats['name'] == "pysduck":
          json.dumps(json_Psyduck)
        if secondpokemon_stats['name'] == "pidove":
          json.dumps(json_Pidove)
        if secondpokemon_stats['name'] == "rattata":
          json.dumps(json_Rattata)
      if rid =="3":
        third = "None"
        print("You Got Rid Of Your Third Pokemon")
        if thirdpokemon_stats['name'] == "pysduck":
          json.dumps(json_Psyduck1)
        if thirdpokemon_stats['name'] == "pidove":
          json.dumps(json_Pidove1)
        if thirdpokemon_stats['name'] == "rattata":
          json.dumps(json_Rattata1)
      else:
        print("Invalid Input")
    if freechoice == "10":
      print("Bye")
      break
  break
print("Thanks for playing Pokemon Light!")
print("You collected", totalcoins, "coins in total.")
