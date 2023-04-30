from uuid import uuid4
from sqlalchemy.future import select
from sqlalchemy import delete, update

from carteira_investimentos.database.config import async_session
from carteira_investimentos.database.models.models import AtivosCarteira

from carteira_investimentos.schemas.schemas import AtivosCarteiraCreate


class AtivosCarteiraService:

    async def select_ativos_carteira(id_carteira: str):
        async with async_session() as session:
            ativos_list = await session.execute(select(AtivosCarteira).where(AtivosCarteira.carteira_id == id_carteira))
            ativos_list = ativos_list.scalars().all()
            return ativos_list

    async def create_ativos_carteira(id_carteira: str, ativos_carteira: AtivosCarteiraCreate):
        async with async_session() as session:
            ativo_create = AtivosCarteira(
                id=str(uuid4()),
                codigo_ativo=ativos_carteira.codigo_ativo,
                preco_medio=ativos_carteira.preco_medio,
                quantidade_ativos=ativos_carteira.quantidade_ativos,
                preco_atual=ativos_carteira.preco_atual,
                status_em_carteira=ativos_carteira.status_em_carteira,
                carteira_id=id_carteira
            )
            session.add(ativo_create)
            await session.commit()
            return ativo_create

    async def select_ativos_carteira_id(id_ativos_carteira: str):
        async with async_session() as session:
            operacao_list = await session.execute(select(AtivosCarteira).where(AtivosCarteira.id == id_ativos_carteira))
            results = operacao_list.scalars().first()
            return results
        
    async def update_carteira_id(id_ativo, ativos_carteira):
        async with async_session() as session:
            await session.execute(update(AtivosCarteira).where(AtivosCarteira.id == id_ativo).values(
                codigo_ativo=ativos_carteira.codigo_ativo,
                preco_medio=ativos_carteira.preco_medio,
                quantidade_ativos=ativos_carteira.quantidade_ativos,
                preco_atual=ativos_carteira.preco_atual,
                status_em_carteira=ativos_carteira.status_em_carteira
            ))
            await session.commit()
            return ativos_carteira
            
    async def delete_ativos_carteira_id(id_ativo):
        async with async_session() as session:
            ativos_list = await session.execute(select(AtivosCarteira).where(AtivosCarteira.id == id_ativo))
            results = ativos_list.scalars().one()
            await session.execute(delete(AtivosCarteira).where(AtivosCarteira.id == id_ativo))
            await session.commit()
            return {'msg': f'Carteira {results.codigo_ativo} foi removido'}
           