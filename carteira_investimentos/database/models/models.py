import datetime
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from carteira_investimentos.database.config import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)

    carteira = relationship('Carteira', backref='user', lazy='subquery', cascade="all, delete")


class Carteira(Base):
    __tablename__ = "carteira"

    id = Column(String, primary_key=True, index=True)
    patrimonio = Column(Float)
    total_investido = Column(Float)

    user_id = Column(String, ForeignKey('user.id', ondelete="CASCADE"))
    ativos_carteira = relationship('AtivosCarteira', backref='carteira', lazy='subquery')
    operacao = relationship('Operacao', backref='carteira', lazy='subquery')


class AtivosCarteira(Base):
    __tablename__ = "ativos_carteira"

    id = Column(String, primary_key=True, index=True)
    codigo_ativo = Column(String)
    preco_medio = Column(Float)
    quantidade_ativo = Column(Integer)
    status_em_carteira = Column(Integer)
    preco_atual = Column(Float)

    carteira_id = Column(String, ForeignKey('carteira.id', ondelete="CASCADE"))
    

class Operacao(Base):
    __tablename__ = "operacao"
    
    id = Column(String, primary_key=True, index=True)
    codigo_ativo = Column(String)
    tipo_operacao = Column(String)
    valor_operacao = Column(Float)
    quantidade_ativo = Column(Integer)
    data_operacao = Column(DateTime, default=datetime.datetime.utcnow)

    carteira_id = Column(String, ForeignKey('carteira.id', ondelete="CASCADE"))