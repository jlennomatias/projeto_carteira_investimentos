from carteira_investimentos.database.config import async_session

async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()