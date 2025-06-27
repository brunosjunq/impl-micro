# Agenda de Contatos – API REST com FastAPI

Pequeno projeto‐exemplo de microsserviço para gerenciar **Contatos** usando **FastAPI** (Python 3.10+).  
Oferece operações de **inclusão, consulta** e **listagem** de contatos, ilustradas por um script de teste em `tests/demo_requests.py`.

---

## Funcionalidades

- **POST /contacts** – cria um novo contato  
- **GET /contacts/{id}** – obtém um contato pelo ID  
- **GET /contacts** – lista todos os contatos cadastrados  
- Validação automática de dados com **Pydantic**  
- Enumerações para tipo de telefone (`MOVEL`, `FIXO`, `COMERCIAL`) e categoria (`FAMILIAR`, `PESSOAL`, `COMERCIAL`)  
- Banco de dados **em memória** para simplificar; fácil de trocar por SQLite/PostgreSQL

---

## Estrutura de diretórios
contact_service/
├─ app.py # Endpoints FastAPI
├─ models.py # Enumerações e “banco” em memória
├─ schemas.py # Esquemas/validação Pydantic
└─ tests/
└─ demo_requests.py # Script demonstrativo

---

## Pré-requisitos

- Python 3.10 ou superior  
- (Opcional) **virtualenv** para isolar dependências

---

## Instalação & execução

## 1. Clone o repositório
git clone https://github.com/<seu-usuario>/contact_service.git
cd contact_service

## 2. Crie o ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## 3. Instale as dependências
pip install fastapi uvicorn[standard] pydantic requests

## 4. Rodando o servidor
python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000

---

## Teste rápido

## a. Via cURL

## Criar contato

curl -X POST http://127.0.0.1:8000/contacts \
    -H "Content-Type: application/json" \
    -d '{"nome":"Alice",
         "telefones":[{"numero":"71-91234-5678","tipo":"MOVEL"}],
         "categoria":"PESSOAL"}'

## b. Via script

## Executar script demo

python tests/demo_requests.py

## Saída típica:

Criado: {'id': '...', 'nome': 'Alice', ...}
Consulta: {'id': '...', 'nome': 'Alice', ...}
Lista: [
  {
    "id": "...",
    "nome": "Alice",
    "telefones": [...],
    "categoria": "PESSOAL"
  }
]

## Listar

curl http://127.0.0.1:8000/contacts
