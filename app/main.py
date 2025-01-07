from fastapi import FastAPI
from app.api.ads import router as ads_router
from loguru import logger

app = FastAPI()

app.include_router(ads_router, prefix="/api/v1/ads", tags=["Meta Ads"])
