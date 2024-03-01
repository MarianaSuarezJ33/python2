from fastapi import APIRouter, HTTPException
from . import crud, schemas

router = APIRouter()

@router.post("/pokemon/", response_model=schemas.Pokemon)
def create_pokemon(pokemon: schemas.PokemonCreate):
    return crud.create_pokemon(pokemon)

@router.get("/pokemon/{pokemon_id}", response_model=schemas.Pokemon)
def read_pokemon(pokemon_id: str):
    pokemon = crud.get_pokemon(pokemon_id)
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@router.put("/pokemon/{pokemon_id}", response_model=schemas.Pokemon)
def update_pokemon(pokemon_id: str, pokemon: schemas.PokemonUpdate):
    updated_pokemon = crud.update_pokemon(pokemon_id, pokemon)
    if updated_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return updated_pokemon

@router.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: str):
    deleted_pokemon = crud.delete_pokemon(pokemon_id)
    if deleted_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return {"message": "Pokemon deleted successfully"}
