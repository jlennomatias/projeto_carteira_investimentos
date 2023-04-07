from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from carteira_investimentos.controllers.depends import get_current_user
from carteira_investimentos.controllers.crud.ativos_carteira_controllers import AtivosCarteiraService
from carteira_investimentos.schemas.schemas import AtivosCarteiraCreate, AtivosCarteiraView


router = APIRouter(tags=["AtivosCarteira"])



@router.get('/ativos_carteira', response_model=List[AtivosCarteiraView])
async def get_ativos_carteira():
    try:
        ativos_carteira = await AtivosCarteiraService.select_ativos_carteira()
        if not ativos_carteira:
            raise HTTPException(status_code=404, detail="Item not found")
        return ativos_carteira
    except Exception as error:
        raise error


@router.post('/ativos_carteira', response_model=AtivosCarteiraCreate)
async def create_ativos_carteira(id_carteira: str, ativos_carteira: AtivosCarteiraCreate):
    try:
        ativos_carteira = await AtivosCarteiraService.create_ativos_carteira(id_carteira=id_carteira, ativos_carteira=ativos_carteira)
        return ativos_carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.get('/ativos_carteira/{id_ativos_carteira}', response_model=AtivosCarteiraView)
async def get_ativos_carteira_id(
    id_ativos_carteira: str):
    try:
        ativos_carteira = await AtivosCarteiraService.select_ativos_carteira_id(id_ativos_carteira=id_ativos_carteira)
        if not ativos_carteira:
            raise HTTPException(status_code=404, detail="Item not found")
        return ativos_carteira
    except Exception as error:
        raise error


@router.put('/ativos_carteira/{id_ativos_carteira}', response_model=AtivosCarteiraView)
async def update_ativos_carteira(id_ativos_carteira: str, ativos_carteira: AtivosCarteiraCreate):
    try:
        ativos_carteira = await AtivosCarteiraService.update_ativos_carteira_id(id_ativos_carteira=id_ativos_carteira, ativos_carteira=ativos_carteira)
        if not ativos_carteira:
            raise HTTPException(status_code=404, detail="Item not found")
        return ativos_carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@router.delete('/ativos_carteira/{id_ativos_carteira}')
async def delete_ativos_carteira_id(id_ativos_carteira: str):
    try:
        ativos_carteira = await AtivosCarteiraService.delete_ativos_carteira_id(id_ativo=id_ativos_carteira)
        if not ativos_carteira:
            raise HTTPException(status_code=404, detail="Item not found")
        return ativos_carteira
    except Exception as error:
        raise HTTPException(400, detail=str(error))