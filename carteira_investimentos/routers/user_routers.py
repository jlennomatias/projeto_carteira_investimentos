from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from carteira_investimentos.controllers.depends import get_current_user
from carteira_investimentos.controllers.security.auth import verify_password, create_access_token
from carteira_investimentos.controllers.crud.user_controllers import UserService
from carteira_investimentos.schemas.schemas import UserView, UserCreate, UserCreateView
from carteira_investimentos.shared.excepctions import NotFound

router = APIRouter(tags=["User"])


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.get_username(username=form_data.username)
    if not user or not verify_password(form_data.password, user.senha):
        raise HTTPException(status_code=403, detail="User ou senha incorretos")
    user = {
        "id": user.id,
        "nome": user.nome
    }
    return {
        "access_token": create_access_token(user, 30),
        "token_type": "bearer",
    }


@router.get('/login', response_model=List[UserView])
async def get_user(usuario_logado: OAuth2PasswordRequestForm = Depends(get_current_user)):
    usuario = await UserService.select_user()
    return usuario


@router.get('/user', response_model=List[UserView])
async def get_user():
    usuario = await UserService.select_user()
    return usuario


@router.post('/user', response_model=UserCreateView)
async def create_user(user: UserCreate):
    try:
        usuario = await UserService.create_user(user=user)
        return usuario
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.get('/user/{id_user}', response_model=UserView)
async def get_user_id(
    id_user: str):
    try:
        usuario = await UserService.select_user_id(id_user=id_user)
        if not usuario:
            raise NotFound("ativo")
        return usuario
    except Exception as error:
        raise error


@router.put('/user/{id_user}')
async def update_user_id(id_user: str, user: UserCreate):
    try:
        usuario = await UserService.atualizar_user_id(id_user=id_user, user=user)
        return usuario
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@router.delete('/user/{id_user}')
async def delete_user_id(id_user: str):
    try:
        usuario = await UserService.delete_user_id(id_user=id_user)
        return usuario
    except Exception as error:
        raise HTTPException(400, detail=str(error))