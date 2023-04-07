from uuid import uuid4
from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError

from carteira_investimentos.database.config import async_session
from carteira_investimentos.database.models.models import AtivosCarteira

from carteira_investimentos.schemas.schemas import AtivosCarteiraCreate


class AtivosCarteiraService:

    async def select_ativos_carteira(**kwargs):
        async with async_session() as session:
            ativos_list = await session.execute(select(AtivosCarteira))
            ativos_list = ativos_list.scalars().all()
            return ativos_list

    async def create_ativos_carteira(id_carteira: str, ativos_carteira: AtivosCarteiraCreate):
        async with async_session() as session:
            ativo_create = AtivosCarteira(
                id=str(uuid4()),
                codigo_ativo=ativos_carteira.codigo_ativo,
                preco_medio=ativos_carteira.preco_medio,
                quantidade_ativo=ativos_carteira.quantidade_ativo,
                status_em_carteira=ativos_carteira.status_em_carteira,
                preco_atual=ativos_carteira.preco_atual,
                carteira_id=id_carteira
            )
            print(f"Criando o meus_ativos de id: {ativo_create.id}")
            session.add(ativo_create)
            await session.commit()
            return ativo_create
            
    async def update_carteira_id(id_carteira, ativos_carteira):
        async with async_session() as session:
            await session.execute(update(AtivosCarteira).where(AtivosCarteira.id == id_carteira).values(
                codigo_ativo=ativos_carteira.codigo_ativo,
                preco_medio=ativos_carteira.preco_medio,
                quantidade_ativo=ativos_carteira.quantidade_ativo,
                status_em_carteira=ativos_carteira.status_em_carteira,
                preco_atual=ativos_carteira.preco_atual
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
           