from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from carteira_investimentos.controllers.depends import get_current_user
from carteira_investimentos.controllers.crud.carteira_controllers import CarteiraService
from carteira_investimentos.schemas.schemas import CarteiraView, CarteiraCreate

router = APIRouter(tags=["Carteira"])



@router.get('/carteira', response_model=List[CarteiraView])
async def get_carteira():
    carteira = await CarteiraService.select_carteira()
    return carteira


@router.post('/carteira', response_model=CarteiraCreate)
async def create_carteira(carteira: CarteiraCreate, user_id: str):
    try:
        carteira = await CarteiraService.create_carteira(carteira=carteira, user_id=user_id)
        return carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.get('/carteira/{id_carteira}', response_model=CarteiraView)
async def get_carteira_id(
    id_carteira: str):
    try:
        carteira = await CarteiraService.select_carteira_id(id_carteira=id_carteira)
        if not carteira:
            raise HTTPException(status_code=404, detail="Item not found")
        return carteira
    except Exception as error:
        raise error


@router.put('/carteira/{id_carteira}', response_model=CarteiraView)
async def update_carteira(id_carteira: str, carteira: CarteiraCreate):
    try:
        carteira = await CarteiraService.update_carteira_id(id_carteira=id_carteira, carteira=carteira)
        return carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@router.delete('/carteira/{id_carteira}')
async def delete_carteira_id(id_carteira: str):
    try:
        carteira = await CarteiraService.update_carteira_id(id_carteira=id_carteira)
        return carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))