import requests, json

BASE = "http://127.0.0.1:8000"

novo = {
    "nome": "Alice",
    "telefones": [
        {"numero": "71-91234-5678", "tipo": "MOVEL"},
        {"numero": "71-4002-8922", "tipo": "COMERCIAL"}
    ],
    "categoria": "PESSOAL"
}

# inclusão
r = requests.post(f"{BASE}/contacts", json=novo)
print("Criado:", r.json())

cid = r.json()["id"]

# consulta
r = requests.get(f"{BASE}/contacts/{cid}")
print("Consulta:", r.json())

# listagem
r = requests.get(f"{BASE}/contacts")
print("Lista:", json.dumps(r.json(), indent=2, ensure_ascii=False))
