from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.database import *
from app.server.models.produto import *

router = APIRouter()


@router.post('/', response_description='Adiciona um novo produto no banco de dados')
async def create_produto_data(produto: ProdutoSchema = Body(...)):
    produto = jsonable_encoder(produto)
    new_produto = await create_produto(produto)
    return ResponseModel(new_produto, 'Produto criado com sucesso.')


@router.get('/', response_description="Lista todos os produtos presentes no banco de dados")
async def get_produtos():
    produtos = await read_produtos()
    if produtos:
        return ResponseModel(produtos, 'Lista de produtos adquirida com sucesso')
    return ResponseModel(produtos, 'Lista vazia retornada')


@router.get('/{id}', response_description="Lista um produto passando seu ID")
async def get_produto_data(id):
    produto = await read_produto(id)
    if produto:
        return ResponseModel(produto, 'Produto listado com sucesso')
    return ErrorResponseModel('Um erro ocorreu', 404, 'Produto não existe.')


@router.put("/{id}")
async def update_produto_data(id: str, req: UpdateProdutoModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_produto = await update_produto(id, req)
    if updated_produto:
        return ResponseModel(
            "Produto com ID: {} atualizado com sucesso".format(id),
        )
    return ErrorResponseModel(
        "Um erro ocorreu",
        404,
        "Houve um erro ao tentar atualizar os dados do produto.",
    )


@router.delete('/{id}', response_description="Deleta produto do banco de dados")
async def delete_produto_data(id: str):
    deleted_produto = await delete_produto(id)
    if deleted_produto:
        return ResponseModel(
            f"Produto with ID: {id} removed",
            "Produto deleted successfully"
        )
    return ErrorResponseModel(
        "An error ocurred", 404, "Produto with id {0} doesn't exist"
    )
