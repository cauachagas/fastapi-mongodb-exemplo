def produto_helper(produto) -> dict:
    return {
        "id": str(produto["_id"]),
        "nome": produto["nome"],
        "preco": produto["preco"],
    }
