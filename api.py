from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de dados
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# "Banco de dados" em memória
usuarios = []

# Endpoint para listar usuários
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

# Endpoint para cadastrar novo usuário
@app.post("/usuarios", response_model=Usuario)
def cadastrar_usuario(usuario: Usuario):
    for u in usuarios:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já cadastrado.")
    usuarios.append(usuario)
    return usuario