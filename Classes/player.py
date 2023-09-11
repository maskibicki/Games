from pydantic import BaseModel
from Classes.pokemon import Pokemon

class Player(BaseModel):
    name: str = ""
    coins: int = 5
    lifetime_coins: int = 5
    stage_price: int = 5
    level: int = 5
    pokeballs: int = 20
    potions: int = 5
    wandermax: int = 0
    pokemon: list[Pokemon] = []