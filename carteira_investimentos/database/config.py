from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

postgresql_url = "postgresql+asyncpg://admin:psltest@192.168.59.100:30356/postgresdb"

Base = declarative_base()

#Criando uma instancia de banco de dados chamada "engine"
engine = create_async_engine(postgresql_url, echo=False, future=True)

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