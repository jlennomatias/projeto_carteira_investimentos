import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field


class EnumTipoOperacao(str, Enum):
    COMPRA = 'COMPRA'
    VENDA = 'VENDA'

class OperacaoCreate(BaseModel):
    codigo_ativo: str
    tipo_operacao: EnumTipoOperacao = Field(
        ...,
        description='Tipo de operação, se foi realizado uma compra ou venda',
        example='COMPRA',
    )
    valor_operacao: Optional[float]
    quantidade_ativo: Optional[int]
    data_operacao: Optional[datetime.date]


    class Config:
        orm_mode = True


class OperacaoView(BaseModel):
    id: str
    codigo_ativo: str
    tipo_operacao: EnumTipoOperacao = Field(
        ...,
        description='Tipo de operação, se foi realizado uma compra ou venda',
        example='COMPRA',
    )
    valor_operacao: Optional[float]
    quantidade_ativo: Optional[int]
    data_operacao: Optional[datetime.date]

    carteira_id: str

    class Config:
        orm_mode = True


class AtivosCarteiraCreate(BaseModel):
    codigo_ativo: str = None
    preco_medio: float = 0.0
    quantidade_ativos: int = 0
    preco_atual: float = 0.0
    status_em_carteira: bool = True

    class Config:
        orm_mode = True


class AtivosCarteiraView(BaseModel):
    id: Optional[str]
    codigo_ativo: str = None
    preco_medio: float = 0.0
    quantidade_ativos: int = 0
    preco_atual: float = 0.0
    status_em_carteira: bool = True

    class Config:
        orm_mode = True


class CarteiraCreate(BaseModel):
    patrimonio: float = 0.0
    total_investido: float = 0.0

    class Config:
        orm_mode = True


class CarteiraView(BaseModel):
    id: str
    patrimonio: float
    total_investido: float
    user_id: str

    ativos_carteira: Optional[List[AtivosCarteiraView]]
    operacao: Optional[List[OperacaoView]]

    class Config:
        orm_mode = True


class CarteiraViewUser(BaseModel):
    patrimonio: float
    total_investido: float

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