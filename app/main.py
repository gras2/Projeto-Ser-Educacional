from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api.ads import router as ads_router
from loguru import logger
from pathlib import Path
from fastapi.responses import HTMLResponse

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

# Criando diretório para logs, se não existir
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Configuração de logs usando loguru
log_file_path = log_dir / "logfile.log"
logger.add(log_file_path, rotation="1 MB", retention="10 days", level="INFO")
logger.info("API inicializada com sucesso.")

# Adicionando roteadores
try:
    app.include_router(ads_router, prefix="/ads", tags=["Meta Ads"])
    logger.info("Roteador de anúncios incluído com sucesso.")
except Exception as e:
    logger.error(f"Erro ao incluir roteador de anúncios: {e}")

# Endpoint raiz
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Endpoint de status
@app.get("/status")
async def status():
    return {"status": "ok", "message": "API está operacional."}