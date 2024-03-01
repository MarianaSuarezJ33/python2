from typing import List, Optional
from pydantic import ObjectId
from .schemas import Item, ItemCreate

# Importar la conexión MongoDB
from .database import mongo

# Colección en la base de datos MongoDB
collection = mongo.db.items

# Función para obtener todos los items
def get_items() -> List[Item]:
    return [Item(**item) for item in collection.find()]

# Función para obtener un item por su ID
def get_item(item_id: str) -> Optional[Item]:
    item_data = collection.find_one({"_id": ObjectId(item_id)})
    return Item(**item_data) if item_data else None

# Función para crear un nuevo item
def create_item(item: ItemCreate) -> Item:
    item_data = item.dict()
    item_id = collection.insert_one(item_data).inserted_id
    return get_item(str(item_id))

# Función para actualizar un item existente
def update_item(item_id: str, item: ItemCreate) -> Optional[Item]:
    item_data = item.dict()
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
    if result.modified_count:
        return get_item(item_id)
    return None

# Función para eliminar un item por su ID
def delete_item(item_id: str) -> Optional[Item]:
    item = get_item(item_id)
    if item:
        collection.delete_one({"_id": ObjectId(item_id)})
    return item
