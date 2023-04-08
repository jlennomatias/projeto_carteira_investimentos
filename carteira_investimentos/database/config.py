from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

postgresql_url = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"

Base = declarative_base()

#Criando uma instancia de banco de dados chamada "engine"
engine = create_async_engine(postgresql_url, echo=False, future=True)

#Definindo o objeto de sessão e informando que será assincrono
async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )