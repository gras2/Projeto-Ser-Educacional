from loguru import logger  # Importa o logger para registrar logs durante os testes
from fastapi.testclient import TestClient  # Importa a classe TestClient do FastAPI para testar rotas da API
from app.main import app  # Importa a aplicação FastAPI principal

client = TestClient(app)  # Cria um cliente de teste com a instância da aplicação FastAPI

# Função de teste para o endpoint "/ads"
def test_fetch_ads_data():
    # Envia uma solicitação GET para o endpoint "/ads" com o parâmetro de consulta 'campaign_id=12345'
    response = client.get("/ads/?campaign_id=12345")
    
    # Verifica se o código de status da resposta é 200 (OK)
    assert response.status_code == 200
