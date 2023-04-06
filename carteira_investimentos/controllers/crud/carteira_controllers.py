from fastapi import HTTPException, status
from sqlalchemy.future import select
from uuid import uuid4
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError

from carteira_investimentos.database.models.models import Carteira
from carteira_investimentos.database.config import async_session
from carteira_investimentos.schemas.schemas import CarteiraCreate
from carteira_investimentos.controllers.crud.operacao_controllers import OperacaoService
from carteira_investimentos.controllers.utils.carteira_utils import CarteiraUtils


class CarteiraService:

    async def select_carteira(**kwargs):
        async with async_session() as session:
            carteira_result = await session.execute(select(Carteira))
            carteira_result = carteira_result.scalars().all()
            return carteira_result

    async def create_carteira(carteira: CarteiraCreate):
        async with async_session() as session:
            carteira = Carteira(
                id=str(uuid4()),
                patrimonio=carteira.patrimonio,
                total_investido=carteira.total_investido,
                user_id=carteira.user_id
            )
            try:
                session.add(carteira)
                await session.commit()
                return carteira
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='carteira already exists'
                )
    
    async def select_carteira_id(id_carteira):
        async with async_session() as session:
            carteira_list = await session.execute(select(Carteira).where(Carteira.id == id_carteira))
            carteira_result = carteira_list.scalars().first()
            print(f"imprimindo {type(carteira_result)}")
            carteira_result.total_investido = await CarteiraUtils.calc_total_investido(carteira_result.total_investido)
            
            return carteira_result
        

    async def update_carteira_id(id_carteira, carteira: CarteiraCreate):
        async with async_session() as session:
            await session.execute(update(Carteira).where(Carteira.id == id_carteira).values(
                patrimonio=carteira.patrimonio,
                total_investido=carteira.total_investido,
                user_id=carteira.user_id
            ))
            await session.commit()
            return carteira

        
    async def delete_carteira_id(id_carteira):
        async with async_session() as session:
            carteira_list = await session.execute(select(Carteira).where(Carteira.id == id_carteira))
            results = carteira_list.scalars().one()
            await session.execute(delete(Carteira).where(Carteira.id == id_carteira))
            await session.commit()
            return {'msg': f'Carteira {results.codigo_carteira} foi removido'}
