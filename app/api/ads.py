from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from app.models import NomeDoModelo

router = APIRouter()

@router.get("/ads_units")
async def get_ads_units():
    return {"message": "Endpoint para obter unidades do Meta Ads"}
