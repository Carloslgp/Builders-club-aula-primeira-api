from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


db_livros = []

indice_atual = 0

class Livro(BaseModel):
    autor: str
    titulo: str
    paginas: int

@app.get("/livros", status_code=200)
def buscar_livros():
    return db_livros

@app.post("/livros")
def adicionar_livro(livro: Livro):
    global indice_atual
    novo_livro = {"id": indice_atual, **livro.model_dump()}
    db_livros.append(novo_livro)
    indice_atual += 1
    return {"mensagem": "Livro adicionado com sucesso!"}

@app.delete("/livros/{id_livro}", status_code=200)
def deletar_livros(id_livro: int):
    for indice, elemento in enumerate(db_livros):
        if(id_livro == elemento["id"]):
            db_livros.pop(indice)
            return {"mensagem": "Livro deletado"}
    raise HTTPException(status_code=404, detail="Não encontrado")
