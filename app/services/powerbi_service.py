#"""
#Serviço responsável por enviar dados ao Power BI.
#- Funções principais:
#  - Preparar dados para envio.
#  - Integrar com a API REST do Power BI.
#"""
#import httpx
#import pandas as pd
#from loguru import logger

#async def send_data_to_powerbi(data: dict) -> dict:
#    async with httpx.AsyncClient() as client:
#        response = await client.post("https://seu-endpoint-powerbi.com", json=data)
#        if response.status_code != 200:
#            raise Exception(f"Erro ao enviar dados para o Power BI: {response.text}")
#        return response.json()