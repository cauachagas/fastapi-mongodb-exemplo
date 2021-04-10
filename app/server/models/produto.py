from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ProdutoSchema(BaseModel):
    nome: str = Field(...)
    preco: float = Field(..., ge=0.05, le=1000000.0)

    class Config:
        schema_extra = {
            'example': {
                'nome': 'Caneta',
                'preco': 2,
            }
        }


class UpdateProdutoModel(BaseModel):
    nome: Optional[str]
    preco: Optional[str]
    
    class Config:
        schema_extra = {
            'example': {
                'nome': 'Caneta',
                'preco': 3,
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def ErrorResponseModel(error, code, message):
    return {'error': error, 'code': code, 'message': message}
