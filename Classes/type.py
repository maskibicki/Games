from pydantic import BaseModel

class poke_type:
    name: str
    weak: list[str]
    strong: list[str]