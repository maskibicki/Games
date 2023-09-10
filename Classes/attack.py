from pydantic import (
    BaseModel,
    FieldValidationInfo,
    ValidationError,
    field_validator,
)

class Attack(BaseModel):
    name: str
    damage_multiplyer: int = 1
    type: str
    effect: str
    
    @field_validator('effect')
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if v not in ["damage"]:
            raise ValueError("effect %s not a known effect" % ( v ) )
        return v.title()