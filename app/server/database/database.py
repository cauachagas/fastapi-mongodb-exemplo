import os

import motor.motor_asyncio
from bson.objectid import ObjectId
from app.server.database.database_helper import produto_helper

MONGODB_URI = os.environ.get('MONGODB_URI')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

database = client.produtos

produto_collection = database.get_collection('produtos_collection')


# Lista todos os produtos presentes no banco de dados
async def read_produtos():
    produtos = []
    async for produto in produto_collection.find():
        produtos.append(produto_helper(produto))
    return produtos


# Adicionar um novo produto no banco de dados
async def create_produto(produto_data: dict) -> dict:
    produto = await produto_collection.insert_one(produto_data)
    new_produto = await produto_collection.find_one({"_id": produto.inserted_id})
    return produto_helper(new_produto)


# Lista um produto passando seu ID
async def read_produto(id: str) -> dict:
    produto = await produto_collection.find_one({'_id': ObjectId(id)})
    if produto:
        return produto_helper(produto)


# Atualizar um produto passando seu ID
async def update_produto(id: str, data: dict):
    # Retorna falso se o body for vazio
    if len(data) < 1:
        return False
    produto = await produto_collection.find_one({"_id": ObjectId(id)})
    if produto:
        updated_produto = await produto_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_produto:
            return True
        return False

# Deleta um produto do banco de dados
async def delete_produto(id: str):
    produto = await produto_collection.find_one({'_id': ObjectId(id)})
    if produto:
        await produto_collection.delete_one({'_id': ObjectId(id)})
        return True
