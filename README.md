# N703_Integracao_Sistemas

Integração de Sistemas - API REST + Cliente Python

Projeto desenvolvido para a disciplina **N703 - Técnicas de Integração de Sistemas**, com o objetivo de demonstrar uma integração simples e funcional entre dois sistemas usando Python.

## 🛠 Tecnologias Utilizadas

- Python 3
- FastAPI (API)
- Uvicorn (servidor)
- Requests (cliente)
- Swagger (documentação automática da API)

## ⚙️ Funcionalidades da API

- `GET /usuarios` - Lista todos os usuários cadastrados
- `POST /usuarios` - Cadastra um novo usuário
- Dados armazenados em memória (não usa banco)

## 🔗 Simulação de Integração

O arquivo `cliente.py` simula um segundo sistema consumindo a API. Ele envia dados para a API (POST) e busca a lista de usuários (GET), simulando uma integração entre sistemas diferentes.

## ▶️ Como Executar

1. Instale as dependências:
   No terminal:
   pip install fastapi uvicorn requests

2. Rode a API:
uvicorn api:app --reload

3. Acesse o Swagger: http://127.0.0.1:8000/docs

4. Em outro terminal, execute o cliente:
   python cliente.py
