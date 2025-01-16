from pydantic import BaseModel, Field  # Field permite definir validações extras
from typing import List

class AdsData(BaseModel):
    campaign_id: str  # ID da campanha
    impressions: int = Field(..., ge=0, description="Número de impressões deve ser maior ou igual a zero")  # ge: greater or equal
    clicks: int = Field(..., ge=0, description="Número de cliques deve ser maior ou igual a zero")
    spend: float = Field(..., ge=0, description="O gasto deve ser maior ou igual a zero")
