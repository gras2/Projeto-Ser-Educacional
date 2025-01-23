import requests

# Link gerado para teste
url = "https://graph.facebook.com/v21.0/act_264383791293755/insights?time_increment=1&access_token=EAARvDNZAUYcEBO6oGm1oy5pjkT112dRC9g8hN3G84zSRNlx6ZA781l9CVdqZAqINJZAb8zf74qxKoiuiV4zkS4TTNvYXstTvJ9DVZBiW2KaUefmfgZBVw2p5qeA8SqZAoWDzm0adioOVawXZBr5lEtQsntq3PtGwIzLY9Jb7UsobqLpUb2OkbiuPNH0ZCTkinTwhMgsuQ07iOKaBNYjJTwi3TIKL3XgZDZD"

# Fazendo a requisição
response = requests.get(url)

if response.status_code == 200:
    print("Dados obtidos com sucesso:")
    print(response.json())
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)
