import requests

# URL da API
URL_BASE = "http://127.0.0.1:8000/usuarios"

# Novo usuário para cadastro
novo_usuario = {
    "id": 1,
    "nome": "Victor Campos",
    "email": "victor@example.com"
}

# Enviando dados para a API (POST)
resposta_post = requests.post(URL_BASE, json=novo_usuario)

if resposta_post.status_code == 200:
    print("Usuário cadastrado com sucesso:")
    print(resposta_post.json())
else:
    print("Erro ao cadastrar:", resposta_post.text)

# Consultando lista de usuários (GET)
resposta_get = requests.get(URL_BASE)

if resposta_get.status_code == 200:
    print("\nUsuários cadastrados:")
    for usuario in resposta_get.json():
        print(usuario)
else:
    print("Erro ao buscar usuários:", resposta_get.text)
