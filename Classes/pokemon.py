from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    current_hp: int
    max_hp: int
    hp_per_level: int
    attack: int
    attack_per_level: int
    attacks: list[str]
    level: int
    type: str
    starter_pokemon: bool