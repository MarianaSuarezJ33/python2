from pydantic import BaseModel
from typing import List, Optional

class PokemonBase(BaseModel):
    nombre: str
    tipos: List[str]
    nivel: int
    experiencia: int
    estadisticas: dict
    movimientos: List[str]
    fec_captura: Optional[str]
    en_equipo: Optional[bool]

class PokemonCreate(PokemonBase):
    pass

class PokemonUpdate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: str

    class Config:
        orm_mode = True
