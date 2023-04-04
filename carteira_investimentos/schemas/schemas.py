import datetime
from typing import Optional, List
from pydantic import BaseModel


class CarteiraCreate(BaseModel):
    patrimonio: float
    total_investido: float
    user_id: str

    class Config:
        orm_mode = True


class CarteiraView(BaseModel):
    id: str
    patrimonio: float
    total_investido: float
    user_id: str

    class Config:
        orm_mode = True


class UserCreateView(BaseModel):
    id: str
    nome: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    nome: str
    senha: str
    
    class Config:
        orm_mode = True


class UserView(BaseModel):
    id: str
    nome: str
    carteira: Optional[List[CarteiraView]]

    class Config:
        orm_mode = True