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

id_atual = 0

db_livros = []

class Livro(BaseModel):
    autor:str
    titulo: str
    paginas: int



@app.get("/livros", status_code=200)
def buscar_livros():
    return db_livros


@app.post("/livros", status_code=200)
def adicionar_livro(livro: Livro):
    global id_atual
    novo_livro = {"id": id_atual, **livro.model_dump()}
    db_livros.append(novo_livro)
    id_atual += 1
    return {"msg": "Livro adicionado com sucesso", "livro": livro}


@app.put("/livros/{id_livro}", status_code=200)
def atualizar_livro(id_livro:int, livro: Livro):
    for indice, elemento in enumerate(db_livros):
        if(elemento["id"] == id_livro):
            db_livros[indice] = {"id": id_livro, **livro.model_dump()}
            return {"msg": "Livro atuaizado com sucesso", "livro": livro}
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id_livro}")
def deletar_livro(id_livro: int):
    for indice, elemento in enumerate(db_livros):
        if(elemento["id"] == id_livro):
            db_livros.pop(indice)
            return {"msg": "Livro deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Livro não encontrado")

