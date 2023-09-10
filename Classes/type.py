from pydantic import BaseModel

class PokeType(BaseModel):
    name: str
    weak: list[str]
    strong: list[str]