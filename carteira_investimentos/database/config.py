from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

sqlite_url = "sqlite+aiosqlite:///carteira_investimentos.db"

Base = declarative_base()

#Criando uma instancia de banco de dados chamada "engine"
engine = create_async_engine(sqlite_url, echo=True, future=True)

#Definindo o objeto de sessão e informando que será assincrono
async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

def get_db_session():
    try:
        session = async_session()
        yield session
    finally:
        session.close()