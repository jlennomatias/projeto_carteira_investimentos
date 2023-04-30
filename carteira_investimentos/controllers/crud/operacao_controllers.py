from fastapi import HTTPException, status
from sqlalchemy.future import select
from uuid import uuid4
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError

from carteira_investimentos.database.models.models import Operacao
from carteira_investimentos.database.config import async_session
from carteira_investimentos.schemas.schemas import OperacaoCreate
from carteira_investimentos.controllers.utils.ativos_carteira import AtivosUtils

class OperacaoService:

    async def select_operacao(**kwargs):
        async with async_session() as session:
            results = await session.execute(select(Operacao))
            results = results.scalars().all()
            return results
    
    async def select_operacao_carteira(id_carteira: str):
        async with async_session() as session:
            results = await session.execute(select(Operacao).where(Operacao.carteira_id == id_carteira))
            results = results.scalars().all()
            return results

    async def create_operacao(operacao: OperacaoCreate, id_carteira: str):
        async with async_session() as session:
            operacao = Operacao(
                carteira_id=id_carteira,
                id=str(uuid4()),
                codigo_ativo=operacao.codigo_ativo,
                tipo_operacao=operacao.tipo_operacao,
                valor_operacao=operacao.valor_operacao,
                quantidade_ativo=operacao.quantidade_ativo,
                data_operacao=operacao.data_operacao
            )
            try:
                session.add(operacao)
                await session.commit()
                ativos_carteira = AtivosUtils(id_carteira)
                await ativos_carteira.cadastrar_ativos_carteira(operacao)
                
                return operacao
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='operacao already exists'
                )
    
    async def select_operacao_id(id_operacao: str):
        async with async_session() as session:
            operacao_list = await session.execute(select(Operacao).where(Operacao.id == id_operacao))
            results = operacao_list.scalars().first()
            return results
    

    async def update_operacao_id(id_operacao, operacao: OperacaoCreate):
        async with async_session() as session:
            await session.execute(update(Operacao).where(Operacao.id == id_operacao).values(
                carteira_id=operacao.carteira_id,
                codigo_ativo=operacao.codigo_ativo,
                tipo_operacao=operacao.tipo_operacao,
                valor_operacao=operacao.valor_operacao,
                quantidade_ativo=operacao.quantidade_ativo,
                data_operacao=operacao.data_operacao
            ))
            await session.commit()
            operacao_list = await session.execute(select(Operacao).where(Operacao.id == id_operacao))
            return operacao_list.scalars().first()

        
    async def delete_operacao_id(id_operacao):
        async with async_session() as session:
            operacao_list = await session.execute(select(Operacao).where(Operacao.id == id_operacao))
            results = operacao_list.scalars().one()
            await session.execute(delete(Operacao).where(Operacao.id == id_operacao))
            await session.commit()
            return {'msg': f'Operacao {results.codigo_ativo} foi removido'}
