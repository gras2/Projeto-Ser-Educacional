import pandas as pd
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from app.models.ads_model import AdsData
from config.settings import settings
import requests
from fastapi import HTTPException
import json
import logging

INSIGHTS_DATA = []  # Variável global para armazenar os dados

def load_insights_data(filepath: str) -> list:
    """
    Carrega os dados de insights do arquivo JSON.
    
    Args:
        filepath (str): Caminho para o arquivo JSON.
        
    Returns:
        list: Dados carregados.
    """
    import json

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Log para verificar a estrutura dos dados
        if isinstance(data, list):
            print(f"Dados carregados. Tipo: {type(data)}. Total de registros: {len(data)}.")
            if len(data) > 0 and "data" in data[0]:
                print(f"Exemplo de estrutura interna: {data[0]['data'][:1]}")  # Mostra o primeiro registro
        else:
            print("Estrutura de dados inesperada. Verifique o arquivo JSON.")

        return data

    except Exception as e:
        raise ValueError(f"Erro ao carregar o arquivo JSON: {e}")


def load_insights(filepath):
    global INSIGHTS_DATA
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            INSIGHTS_DATA = json.load(file)
        logging.info(f"Dados carregados com sucesso! Total de registros: {len(INSIGHTS_DATA['data'])}")
    except Exception as e:
        raise Exception(f"Erro ao carregar o arquivo: {str(e)}")

logging.basicConfig(level=logging.INFO)

def filter_data(data: list, adset_id: str = None, date_start: str = None, date_stop: str = None) -> list:
    """
    Filtra os dados de insights com base nos parâmetros fornecidos.
    
    Args:
        data (list): Dados de insights carregados.
        adset_id (str, optional): ID do conjunto de anúncios para filtrar.
        date_start (str, optional): Data inicial para filtrar (YYYY-MM-DD).
        date_stop (str, optional): Data final para filtrar (YYYY-MM-DD).
    
    Returns:
        list: Dados filtrados com base nos critérios fornecidos.
    """
    try:
        filtered_data = data
        
        # Filtrar por adset_id
        if adset_id:
            filtered_data = [item for item in filtered_data if item.get("adset_id") == adset_id]
        
        # Filtrar por data de início
        if date_start:
            filtered_data = [item for item in filtered_data if item.get("date_start") >= date_start]
        
        # Filtrar por data de fim
        if date_stop:
            filtered_data = [item for item in filtered_data if item.get("date_stop") <= date_stop]
        
        return filtered_data
    except Exception as e:
        raise ValueError(f"Erro ao filtrar dados: {e}")



def analyze_data(data: list) -> dict:
    """
    Realiza análise agregada dos dados.
    Args:
        data (list): Dados de insights carregados ou filtrados.
    Returns:
        dict: Resultados da análise.
    """
    total_impressions = sum(int(d.get("impressions", 0)) for d in data)
    total_spend = sum(float(d.get("spend", 0.0)) for d in data)
    return {
        "total_impressions": total_impressions,
        "total_spend": total_spend,
        "average_spend_per_impression": total_spend / total_impressions if total_impressions else 0
    }


async def fetch_data_from_link(link: str) -> dict:
    """
    Faz a requisição ao link gerado e retorna os dados JSON.
    Args:
        link (str): URL completa gerada com token e campos.
    Returns:
        dict: Dados retornados pela API do Meta Ads.
    """
    try:
        response = requests.get(link)
        response.raise_for_status()  # Levanta exceções para status HTTP 4xx/5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao acessar o link: {str(e)}")


# Inicializa a API do Meta Ads
FacebookAdsApi.init(
    access_token=settings.META_ADS_ACCESS_TOKEN,
    app_id=settings.META_APP_ID,
)


async def fetch_ads_data_with_pagination(account_id: str, date_preset: str = "last_30d") -> list[AdsData]:
    """
    Busca dados de anúncios com paginação e retorna uma lista de objetos AdsData.
    Args:
        account_id (str): ID da conta de anúncios.
        date_preset (str, optional): Intervalo de datas (default: "last_30d").
    Returns:
        list[AdsData]: Dados de anúncios paginados.
    """
    fields = [
        'campaign_id', 'campaign_name',
        'adset_id', 'adset_name',
        'ad_id', 'ad_name',
        'impressions', 'clicks', 'spend',
        'date_start', 'date_stop'
    ]
    params = {
        'date_preset': date_preset,
        'time_increment': 1
    }

    all_data = []
    try:
        ad_account = AdAccount(account_id)
        insights = ad_account.get_insights(fields=fields, params=params)

        # Paginação
        while True:
            for record in insights:
                all_data.append(record)
            if 'paging' in insights and 'next' in insights['paging']:
                insights = insights.next()
            else:
                break

    except Exception as e:
        raise ValueError(f"Erro ao buscar dados do Meta Ads: {e}")

    # Converte para objetos AdsData
    return [AdsData(**record) for record in all_data]


async def fetch_insights_data(link: str) -> dict:
    """
    Faz uma requisição ao link gerado e retorna os insights.
    Args:
        link (str): Link completo com token e parâmetros.
    Returns:
        dict: Dados JSON retornados pela API.
    """
    try:
        response = requests.get(link)
        response.raise_for_status()  # Lança exceção para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao acessar o link: {str(e)}")
