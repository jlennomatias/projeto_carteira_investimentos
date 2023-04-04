import datetime
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from carteira_investimentos.database.config import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)

    carteira = relationship('Carteira', backref='user', lazy='subquery')


class Carteira(Base):
    __tablename__ = "carteira"

    id = Column(String, primary_key=True, index=True)
    patrimonio = Column(Float)
    total_investido = Column(Float)

    user_id = Column(String, ForeignKey('user.id'))
