# Importando as dependências necessárias para a aplicação FastAPI
from fastapi import FastAPI
from app.services.ads_service import router as ads_router  # Importando o roteador de anúncios
from app.api.powerbi import powerbi_router  # Importando o roteador de integração com Power BI
from loguru import logger  # Importando o loguru para registros de log
from app.api import ads  # Importando o módulo de anúncios (não está sendo usado diretamente no código, mas pode ser relevante para a estrutura)
import logging  # Importando o módulo de logging padrão do Python
from config.settings import Settings  # Importando as configurações da aplicação (não utilizado diretamente aqui, mas pode ser importante para configurar o ambiente)

# Configuração inicial do FastAPI
app = FastAPI(
    title="Meta Ads API",  # Define o título da API
    description="API para integração de dados do Meta Ads com Power BI",  # Descrição do propósito da API
    version="1.0.0"  # Versão da API
)

# Configuração de logs
logging.basicConfig(level=logging.INFO)  # Configura o nível de log para INFO
logger = logging.getLogger(__name__)  # Cria um logger com o nome do módulo atual (útil para rastrear logs em diferentes módulos)

# Adicionando roteadores
app.include_router(ads_router, prefix="/ads", tags=["Meta Ads"])  # Inclui o roteador de anúncios com prefixo /ads e tags para facilitar a documentação
#app.include_router(powerbi_router, prefix="/powerbi", tags=["Power BI"])  # Inclui o roteador de Power BI com prefixo /powerbi e tags para a documentação

# Endpoint raiz
@app.get("/")  # Define o endpoint raiz para a API
async def root():
    # Retorna uma mensagem simples indicando que a API está funcionando
    return {"message": "API de integração Meta Ads e Power BI funcionando!"}

