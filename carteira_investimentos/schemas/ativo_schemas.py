from pydantic import BaseModel


class AtivoView(BaseModel):
    codigo_ativo: str
    nome_ativo: str
    preco_ativo: float

    class Config:
        orm_mode = True