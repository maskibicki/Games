import json
from Classes.pokemon import Pokemon
from Classes.attack import Attack
from Classes.type import PokeType

def load_game_data():
    print("load attacks")
    with open("data/all_attacks.json", "r") as file:
        base_attack_data = [Attack(**a) for a in json.load(file)]
    
    print("load pokemon")
    with open("data/all_pokemon.json", "r") as file:
        base_pokemon_data = [Pokemon(**p) for p in json.load(file)]
    
    print("load types")
    with open("data/all_types.json", "r") as file:
        base_type_data = [PokeType(**pt) for pt in json.load(file)]
        
    return base_attack_data, base_pokemon_data, base_type_data