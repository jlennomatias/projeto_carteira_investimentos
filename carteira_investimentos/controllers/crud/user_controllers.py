from fastapi import HTTPException, status
from sqlalchemy.future import select
from uuid import uuid4
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError

from carteira_investimentos.controllers.security.auth import create_password
from carteira_investimentos.database.models.models import User
from carteira_investimentos.database.config import async_session
from carteira_investimentos.schemas.schemas import UserCreate
from carteira_investimentos.controllers.crud.carteira_controllers import CarteiraService

class UserService:

    async def get_username(username: str):
        async with async_session() as session:
            user_on_db = await session.execute(select(User).where(User.nome == username))
            if not user_on_db:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user or pass")
            return user_on_db.scalars().first()

    async def create_user(user: UserCreate):
        async with async_session() as session:
            user = User(
                id=str(uuid4()),
                nome=user.nome,
                senha=create_password(user.senha)
            )
            try:
                session.add(user)
                await session.commit()
                return user
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='user already exists'
                )

    async def select_user(**kwargs):
        async with async_session() as session:
            results = await session.execute(select(User))
            return results.scalars().all()
             
    
    async def select_user_id(id_user):
        async with async_session() as session:
            user_list = await session.execute(select(User).where(User.id == id_user))
            results = user_list.scalars().first()
            return results
        
    async def atualizar_user_id(id_user, user: UserCreate):
        async with async_session() as session:
            await session.execute(update(User).where(User.id == id_user).values(
                nome=user.nome,
                senha=create_password(user.senha)
            ))
            await session.commit()
            user_list = await session.execute(select(User).where(User.id == id_user))
            results = user_list.scalars().one()
            return results
        
    async def delete_user_id(id_user):
        async with async_session() as session:
            user_list = await session.execute(select(User).where(User.id == id_user))
            results = user_list.scalars().one()
            await session.execute(delete(User).where(User.id == id_user))
            await session.commit()
            return {'msg': f'Usuario {results.nome} foi removido'}