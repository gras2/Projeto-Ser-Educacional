from app.services.ads_service import load_insights_data

# Caminho para o arquivo JSON
filepath = "D:/Users/gras2/app/projeto_fastapi/app/insights2224.json"

try:
    data = load_insights_data(filepath)
    print(f"Dados carregados com sucesso. Total de registros: {len(data)}")
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
