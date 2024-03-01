from typing import List, Optional
from pydantic import BaseModel

class Movimiento(BaseModel):
    nombre: str
    tipo: str
    poder: int

class Estadisticas(BaseModel):
    nivel: int
    experiencia: int

class PokemonBase(BaseModel):
    nombre: str
    tipos: List[str]
    nivel: int
    experiencia: int
    estadisticas: Estadisticas
    movimientos: List[Movimiento]
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
