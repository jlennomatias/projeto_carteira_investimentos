from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from carteira_investimentos.controllers.depends import get_current_user
from carteira_investimentos.controllers.crud.operacao_controllers import OperacaoService
from carteira_investimentos.schemas.schemas import OperacaoCreate, OperacaoView
from carteira_investimentos.shared.excepctions import NotFound

router = APIRouter(tags=["Operacao"])



@router.get('/operacao')
async def get_operacao():
    try:
        operacao = await OperacaoService.select_operacao()
        if not operacao:
            raise NotFound("ativo")
        return operacao
    except Exception as error:
        raise error

@router.get('/operacao_carteira', response_model=List[OperacaoView])
async def get_operacao_carteira(id_carteira: str):
    try:
        operacao = await OperacaoService.select_operacao_carteira(id_carteira=id_carteira)
        if not operacao:
            raise NotFound("ativo")
        return operacao
    except Exception as error:
        raise error

@router.post('/operacao', response_model=OperacaoCreate)
async def create_operacao(operacao: OperacaoCreate, id_carteira: str):
    try:
        operacao = await OperacaoService.create_operacao(operacao=operacao, id_carteira=id_carteira)
        return operacao
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.get('/operacao/{id_operacao}', response_model=OperacaoView)
async def get_operacao_id(
    id_operacao: str):
    try:
        operacao = await OperacaoService.select_operacao_id(id_operacao=id_operacao)
        if not operacao:
            raise NotFound("ativo")
        return operacao
    except Exception as error:
        raise error


@router.put('/operacao/{id_operacao}', response_model=OperacaoView)
async def update_operacao(id_operacao: str, operacao: OperacaoCreate):
    try:
        operacao = await OperacaoService.update_operacao_id(id_operacao=id_operacao, operacao=operacao)
        if not operacao:
            raise NotFound("ativo")
        return operacao
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@router.delete('/operacao/{id_operacao}')
async def delete_operacao_id(id_operacao: str):
    try:
        operacao = await OperacaoService.delete_operacao_id(id_operacao=id_operacao)
        if not operacao:
            raise NotFound("ativo")
        return operacao
    except Exception as error:
        raise HTTPException(400, detail=str(error))