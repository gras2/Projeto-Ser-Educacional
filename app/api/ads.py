# Importando as dependências necessárias para criar o roteador da API
from fastapi import APIRouter  # Importa a classe APIRouter para criar um roteador de rotas
from fastapi import APIRouter, Depends, HTTPException  # 'Depends' pode ser usado para injeção de dependências e 'HTTPException' para erros HTTP
from app.models import NomeDoModelo  # Importa o modelo de dados 'NomeDoModelo' (não utilizado diretamente no código fornecido)
from app.services.ads_service import fetch_ads_data  # Importa a função 'fetch_ads_data' que pode ser usada para buscar dados (não está sendo usada diretamente aqui)
from app.services.ads_service import get_meta_ads_data  # Importa a função 'get_meta_ads_data' que é usada para obter os dados de campanhas do Meta Ads
from config.settings import settings  # Importa as configurações da aplicação, como o token de acesso do Meta Ads

# Criando uma instância do roteador da API
ads_router = APIRouter()

# Definindo a rota para buscar dados de campanhas do Meta Ads
@ads_router.get("/")  # Define que a rota de GET para o caminho '/' dentro do roteador 'ads_router'
async def fetch_ads_data(campaign_id: str):
    """
    Puxa dados de campanhas do Meta Ads.
    Recebe o ID da campanha como parâmetro e retorna os dados relacionados a essa campanha.
    """
    try:
        # Chama a função para obter dados da campanha, passando o ID da campanha e o token de acesso
        data = await get_meta_ads_data(campaign_id, settings.META_ADS_ACCESS_TOKEN)
        
        # Retorna uma resposta JSON com sucesso e os dados da campanha
        return {"success": True, "data": data}
    except Exception as e:
        # Se ocorrer algum erro durante a execução, levanta uma exceção HTTP com o código 500 e a mensagem de erro
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados: {str(e)}")
