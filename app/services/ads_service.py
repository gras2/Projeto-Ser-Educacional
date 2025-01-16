import httpx
from app.models.ads_model import AdsData
from fastapi import HTTPException

class AdsService():
    @staticmethod
    def fetch_ads_data(campaign_id: str) -> AdsData:
        """
        Simula a obtenção de dados de anúncios.
        Args:
            campaign_id (str): ID da campanha.
        Returns:
            AdsData: Dados simulados de uma campanha.
        """
        if not campaign_id:
            raise ValueError("ID da campanha é obrigatório.")
        return AdsData(
            campaign_id=campaign_id,
            impressions=2000,
            clicks=150,
            spend=100.0
        )

async def get_meta_ads_data(campaign_id: str, access_token: str) -> AdsData:
    """
    Busca dados reais da API do Meta Ads.
    Args:
        campaign_id (str): ID da campanha.
        access_token (str): Token de acesso à API do Meta Ads.
    Returns:
        AdsData: Dados da campanha no formato do modelo.
    """
    # Define a URL da API do Meta Ads
    url = "https://graph.facebook.com/v21.0/act_341867950349467/insights"

    # Define os parâmetros da requisição
    params = {
        "access_token": access_token,
        "fields": "impressions,clicks,spend",
        "filtering": f"[{{'field': 'campaign_id', 'operator': 'EQUAL', 'value': '{campaign_id}'}}]"
    }

    # Faz a requisição usando httpx
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"Erro ao buscar dados: {response.text}")

        # Converte os dados da resposta para o modelo AdsData
        response_data = response.json()
        return AdsData(
            campaign_id=campaign_id,
            impressions=response_data.get("impressions", 0),
            clicks=response_data.get("clicks", 0),
            spend=response_data.get("spend", 0.0)
        )
