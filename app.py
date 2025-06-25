from fastapi import FastAPI, HTTPException, status
from models import add_contact, get_contact, list_contacts
from schemas import ContactIn, ContactOut

app = FastAPI(title="Agenda de Contatos")

@app.post("/contacts", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactIn):
    return add_contact(contact.dict())

@app.get("/contacts/{cid}", response_model=ContactOut)
def read_contact(cid: str):
    contact = get_contact(cid)
    if not contact:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contact

@app.get("/contacts", response_model=list[ContactOut])
def read_contacts():
    return list_contacts()
