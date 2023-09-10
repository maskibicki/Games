from pydantic import BaseModel
from Classes.pokemon import Pokemon

class Player(BaseModel):
    name: str
    coins: int
    lifetime_coins: int
    stage_price: int
    level: int
    pokeballs: int
    potions: int
    wandermax: int
    experience: int
    pokemon: list[Pokemon]