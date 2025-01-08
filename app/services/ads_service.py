"""
Serviço responsável por interagir com a API do Meta Ads.
- Funções principais:
  - Obter unidades da Ser Educacional.
  - Processar dados recebidos.
"""
# Importando as bibliotecas necessárias para a interação com a API e processamento de dados
import httpx  # Biblioteca para fazer chamadas HTTP assíncronas
import pandas as pd  # Biblioteca para manipulação de dados (não usada diretamente neste código, mas possivelmente usada em outros contextos do serviço)
from loguru import logger  # Biblioteca para registro de logs (não utilizada diretamente aqui, mas útil para depuração e monitoramento)
from config.settings import Settings  # Importa as configurações da aplicação, como o token de acesso
from app.models.ads_model import AdsData  # Importa o modelo de dados para representar as informações de anúncios
from fastapi import HTTPException  # Importa a classe HTTPException para lançar erros HTTP personalizados
import requests

# Definindo a classe AdsService, que contém métodos para interagir com a API de anúncios
class AdsService:
    # Método estático para simular a obtenção de dados de anúncios
    @staticmethod
    def fetch_ads_data(campaign_id: str):
        try:
            # Verifica se o ID da campanha foi fornecido
            if not campaign_id:
                raise ValueError("ID da campanha é obrigatório.")  # Lança um erro se o ID da campanha for inválido
            
            # Simulação de resposta com dados de campanha
            return {
                "campaign_id": campaign_id,
                "campaign_name": "Campanha de Exemplo",
                "impressions": 2000
            }
        except ValueError as ve:
            # Captura erros de valor (como quando o ID da campanha está faltando) e retorna uma resposta de erro 400 (Bad Request)
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            # Captura quaisquer outros erros e retorna uma resposta de erro 500 (Erro interno do servidor)
            raise HTTPException(status_code=500, detail="Erro interno no serviço de anúncios.")

# Função assíncrona para obter dados reais da API do Meta Ads
async def get_meta_ads_data(campaign_id: str, access_token: str) -> AdsData:
    # Define a URL da API do Meta Ads para obter os dados de uma campanha específica
    url = f"https://graph.facebook.com/v21.0/act_341867950349467/insights?fields=impressions,clicks,spend,reach&access_token=EAARvDNZAUYcEBO2vBXbb0LZA2Ygkl933soEOBklknzYB4XKgPIizNzUbVkTJAXOuSMpndPSSwhwN4UmhOH8Dy7KNsuSGWnMMNfcnPyZCWwZB1l0SmSdEvyx1G3hKZBY84zUUaqI93ZC7flNdffuOF8RZCNBrlTPYgluX9iRVHgm7qmFZBcv0MaUZAeo4hdFZASei0ArFZAhpVZA8cgp1IK9nv9gQ1hfFoQZDZD"
    
    # Define os parâmetros da requisição, incluindo o token de acesso e os campos solicitados (impressões, cliques, e gastos)
    params = {
        "access_token": access_token,  # O token de acesso da aplicação para autenticação
        "fields": "impressions,clicks,spend"  # Os campos específicos que queremos retornar da API
    }
    
    # Usando o client assíncrono httpx para fazer a requisição
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)  # Envia a requisição GET à API
        if response.status_code != 200:  # Verifica se a resposta não foi bem-sucedida (status diferente de 200)
            # Lança um erro se a resposta da API não for bem-sucedida
            raise Exception(f"Erro ao buscar dados do Meta Ads: {response.text}")
        
        # Retorna os dados da resposta da API, que estão em formato JSON
        return response.json()
