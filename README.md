# Roteiro de Aula - API de Livros com FastAPI


## 1. Criar a pasta do projeto

## 1.1 Criar arquivo main.py


```python

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

```

## 2. Criar o ambiente virtual

```bash
python -m venv venv
```

> O `venv` isola as dependências do projeto, evitando conflitos com outros projetos Python.

---

## 3. Ativar o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

> Você saberá que funcionou quando aparecer `(venv)` no início do terminal.

---

## 4. Instalar as dependências

```bash
pip install fastapi uvicorn
```

- **FastAPI** → framework para criar a API
- **uvicorn** → servidor que vai rodar a aplicação

---


## 6. Rodar o servidor

```bash
uvicorn main:app --reload
```

## 7. Testar a API

Acesse no navegador:

```
http://localhost:8000/docs
```
