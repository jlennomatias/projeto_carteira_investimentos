from fastapi import APIRouter

from carteira_investimentos.controllers.utils.assets import AssetService
from carteira_investimentos.schemas.ativo_schemas import AtivoView


router = APIRouter(tags=["Assets"])



@router.get('/assets', response_model=AtivoView)
async def get_carteira(codigo_ativo: str):
    carteira = await AssetService.list_assets(codigo_ativo)
    return carteira