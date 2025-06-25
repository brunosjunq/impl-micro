from pydantic import BaseModel, Field
from typing import List
from models import PhoneType, Category

class Phone(BaseModel):
    numero: str = Field(..., example="71-99999-8888")
    tipo: PhoneType

class ContactIn(BaseModel):
    nome: str = Field(..., example="Bruno")
    telefones: List[Phone]
    categoria: Category

class ContactOut(ContactIn):
    id: str
