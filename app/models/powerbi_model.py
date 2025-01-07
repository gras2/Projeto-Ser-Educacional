from pydantic import BaseModel

class PowerBIData(BaseModel):
    unit_id: str
    unit_name: str
    impressions: int
    clicks: int
