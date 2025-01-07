from pydantic import BaseModel
from typing import List

class AdUnit(BaseModel):
    id: str
    name: str
    
