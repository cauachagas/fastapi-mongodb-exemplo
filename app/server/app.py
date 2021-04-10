from fastapi import FastAPI

from app.server.routes.produto import router as ProdutoRouter

app = FastAPI()

app.include_router(ProdutoRouter, tags=['Produto'], prefix='/produtos')


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Legal você estar aqui!"}
