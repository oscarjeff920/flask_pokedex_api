from pydantic import BaseModel


class PokedexBase(BaseModel):
    name: str
    description: str
    habitat: str
    isLegendary: bool
