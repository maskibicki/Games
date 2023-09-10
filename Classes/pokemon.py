from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    current_hp: int = 50
    max_hp: int = 50
    hp_per_level: int = 10
    energy: int = 5
    attack: int = 50
    attack_per_level: int = 10
    attacks: list[str]
    level: int = 5
    experience: int = 0
    experience_to_level: int = 10
    type: str
    starter_pokemon: bool = False