from fastapi import FastAPI

app = FastAPI()

# Mini banco de dados
banco_de_dados = {
    "produtos": {
        "1": {"nome": "Produto 1", "descricao": "Descrição do Produto 1"},
        "2": {"nome": "Produto 2", "descricao": "Descrição do Produto 2"},
        "3": {"nome": "Produto 3", "descricao": "Descrição do Produto 3"},
        "4": {"nome": "Produto 4", "descricao": "Descrição do Produto 4"},
        "5": {"nome": "Produto 5", "descricao": "Descrição do Produto 5"},
        "6": {"nome": "Produto 6", "descricao": "Descrição do Produto 6"},
        "7": {"nome": "Produto 7", "descricao": "Descrição do Produto 7"},
        "8": {"nome": "Produto 8", "descricao": "Descrição do Produto 8"},
        "9": {"nome": "Produto 9", "descricao": "Descrição do Produto 9"},
        "10": {"nome": "Produto 10", "descricao": "Descrição do Produto 10"}
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/produto/{id_produto}")
async def get_produto(id_produto: int):
    produto = banco_de_dados["produtos"].get(str(id_produto))
    if produto:
        mensagem = f"Oi, eu sou a requisição número {id_produto}"
        return {"id_produto": id_produto, "mensagem": mensagem, "detalhes": produto}
    else:
        return {"error": "Produto não encontrado"}
