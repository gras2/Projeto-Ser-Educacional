from fastapi import APIRouter, HTTPException, Query
from app.services.ads_service import (
    fetch_ads_data_with_pagination,
    fetch_data_from_link,
    filter_data,
    analyze_data,
)
from app.services.ads_visualization import generate_spend_chart
from app.services.ads_service import INSIGHTS_DATA
import logging

# Inicializando o roteador
ads_router = APIRouter()

@ads_router.get("/fetch")
async def get_insights_from_link(link: str = Query(..., description="URL completa para buscar insights")):
    """
    Endpoint para buscar insights do Meta Ads usando um link gerado.
    Args:
        link (str): URL completa para buscar insights.
    Returns:
        dict: Dados retornados pela API.
    """
    try:
        data = await fetch_data_from_link(link)
        return {"success": True, "data": data}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

@ads_router.get("/data")
async def get_all_data():
    return {"total_records": len(INSIGHTS_DATA['data']), "sample_data": INSIGHTS_DATA['data'][:5]}


@ads_router.get("/filter")
async def filter_ads_data(
    adset_id: str = None, 
    ad_name: str = None, 
    date_start: str = None, 
    date_stop: str = None
):
    """
    Endpoint para filtrar os dados com base nos parâmetros fornecidos.
    Args:
        adset_id (str, optional): ID do conjunto de anúncios.
        ad_name (str, optional): Nome do anúncio.
        date_start (str, optional): Data inicial (YYYY-MM-DD).
        date_stop (str, optional): Data final (YYYY-MM-DD).
    Returns:
        dict: Dados filtrados.
    """
    try:
        logging.info(f"Dados disponíveis: {INSIGHTS_DATA['data'][:5]}")  # Exibe os primeiros 5 registros
        filtered_data = filter_data(INSIGHTS_DATA, adset_id, ad_name, date_start, date_stop)
        return {"success": True, "data": filtered_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao filtrar dados: {str(e)}")



@ads_router.get("/analyze")
async def analyze_ads_data():
    """
    Retorna uma análise agregada dos dados.
    Returns:
        dict: Dados analisados agregados.
    """
    try:
        analysis = analyze_data(INSIGHTS_DATA)
        return {"success": True, "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao analisar os dados: {str(e)}")


@ads_router.get("/visualize")
async def visualize_ads_data():
    """
    Gera um gráfico e retorna o caminho para acessá-lo.
    Returns:
        dict: Caminho do gráfico gerado.
    """
    try:
        output_path = "spend_chart.png"
        generate_spend_chart(INSIGHTS_DATA, f"static/{output_path}")
        return {"success": True, "chart_path": f"/static/{output_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar visualização: {str(e)}")

# Certifique-se de adicionar esta linha no final do arquivo ads.py
router = ads_router
