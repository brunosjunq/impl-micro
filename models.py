from enum import Enum
from uuid import uuid4

class PhoneType(str, Enum):
    movel = "MOVEL"
    fixo = "FIXO"
    comercial = "COMERCIAL"

class Category(str, Enum):
    familiar = "FAMILIAR"
    pessoal = "PESSOAL"
    comercial = "COMERCIAL"

# banco em memória
_db: dict[str, dict] = {}

def add_contact(data: dict) -> dict:
    cid = str(uuid4())
    data["id"] = cid
    _db[cid] = data
    return data

def get_contact(cid: str) -> dict | None:
    return _db.get(cid)

def list_contacts() -> list[dict]:
    return list(_db.values())
