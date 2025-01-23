import requests

# URL do endpoint
url = "http://127.0.0.1:8000/ads/filter"

# Parâmetros para filtragem
params = {
    "adset_id": "23849164162230688",
    "date_start": "2022-01-01",
    "date_stop": "2022-01-02"
}

try:
    # Requisição GET
    response = requests.get(url, params=params)

    # Status da resposta
    print(f"Status Code: {response.status_code}")

    # Conteúdo da resposta
    print("Response JSON:", response.json())
except Exception as e:
    print(f"Erro na requisição: {e}")
