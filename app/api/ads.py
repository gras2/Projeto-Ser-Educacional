from fastapi import APIRouter, HTTPException
from app.services.ads_service import get_meta_ads_data
from config.settings import settings

ads_router = APIRouter()

@ads_router.get("/")
async def get_ads_data(campaign_id: str):
    """
    Busca dados de campanhas do Meta Ads.
    """
    if not campaign_id:
        raise HTTPException(status_code=400, detail="O parâmetro 'campaign_id' é obrigatório.")
    if not settings.META_ADS_ACCESS_TOKEN:
        raise HTTPException(status_code=500, detail="Token de acesso não configurado.")
    try:
        data = await get_meta_ads_data(campaign_id, settings.META_ADS_ACCESS_TOKEN)
        return {"success": True, "data": data.dict()}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados: {str(e)}")

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Ads API funcionando!"}
