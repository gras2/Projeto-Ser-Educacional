from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.api.ads import router as ads_router
from app.services.ads_service import load_insights_data
from loguru import logger
from pathlib import Path
from app.api.ads import router as ads_router


# Caminho para o arquivo JSON com os dados de insights
INSIGHTS_FILEPATH = "D:\\Users\\gras2\\app\\projeto_fastapi\\app\\insights2224.json"  # Substitua pelo caminho correto
INSIGHTS_DATA = []  # Variável global para armazenar os dados carregados

# Configuração inicial do FastAPI
app = FastAPI(
    title="Meta Ads API",
    description="""
    API de Integração Meta Ads

    Esta API foi desenvolvida para fornecer uma integração fácil e eficiente com o Meta Ads.

    Funcionalidades principais:
    - Obtenção de dados de campanhas do Meta Ads, como impressões, cliques e gastos.
    - Validação e manipulação de informações para otimização de campanhas.

    Utilização:
    - Navegue pelos endpoints disponíveis abaixo e explore as funcionalidades interativas.
    """,
    version="1.0.0",
    contact={
        "name": "Equipe Meta Ads API",
        "email": "suporte@metaadsapi.com",
    },
    docs_url="/docs",
    redoc_url="/redoc",
)

# Servir arquivos estáticos (gráficos gerados)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Criando diretório para logs, se não existir
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Configuração de logs usando loguru
log_file_path = log_dir / "logfile.log"
logger.add(log_file_path, rotation="1 MB", retention="10 days", level="INFO")
logger.info("API inicializada com sucesso.")

# Evento de inicialização da API
@app.on_event("startup")
async def startup_event():
    """
    Carrega os dados do arquivo JSON na inicialização da API.
    """
    global INSIGHTS_DATA
    try:
        INSIGHTS_DATA = load_insights_data(INSIGHTS_FILEPATH)
        logger.info(f"Dados carregados com sucesso! Total de registros: {len(INSIGHTS_DATA)}")
    except Exception as e:
        logger.error(f"Erro ao carregar os dados: {e}")

# Adicionando roteadores
try:
    app.include_router(ads_router, prefix="/ads", tags=["Meta Ads"])
    logger.info("Roteador de anúncios incluído com sucesso.")
except Exception as e:
    logger.error(f"Erro ao incluir roteador de anúncios: {e}")

# Endpoint raiz
@app.get("/", response_class=HTMLResponse)
async def home():
    """
    Retorna a página HTML estática da aplicação.
    """
    try:
        with open("static/index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Arquivo index.html não encontrado</h1>", status_code=404)

# Endpoint de status
@app.get("/status")
async def status():
    """
    Verifica o status da API.
    """
    return {"status": "ok", "message": "API está operacional."}
