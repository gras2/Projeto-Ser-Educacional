from pydantic import BaseModel  # Importa a classe BaseModel do Pydantic para validação de modelos de dados
from typing import List  # Importa o tipo List para indicar listas de itens, caso necessário

# Definição do modelo de dados AdsData
class AdsData(BaseModel):
    # Define as propriedades do modelo de dados de anúncios
    campaign_id: str  # ID da campanha (string)
    impressions: int  # Número de impressões (inteiro)
    clicks: int  # Número de cliques (inteiro)
    spend: float  # Gasto com a campanha (número decimal)
