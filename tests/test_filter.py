from app.services.ads_service import load_insights_data, filter_data

# Caminho para o arquivo JSON
FILEPATH = "D:\\Users\\gras2\\app\\projeto_fastapi\\app\\insights2224.json"

def print_sample_data(data):
    """
    Imprime uma amostra dos dados carregados para inspecionar a estrutura.
    """
    print(f"Dados carregados. Tipo: {type(data)}. Total de registros: {len(data)}.")
    if isinstance(data, list) and len(data) > 0:
        print(f"Exemplo de registro: {data[0]}")
    else:
        print("Os dados estão vazios ou não são uma lista.")

def normalize_data(raw_data):
    """
    Normaliza os dados para acessar corretamente os campos aninhados.
    """
    if isinstance(raw_data, list):
        normalized = []
        for entry in raw_data:
            if "data" in entry and isinstance(entry["data"], list):
                normalized.extend(entry["data"])  # Desaninha os dados
        return normalized
    return raw_data

def run_tests():
    try:
        # Carregar dados
        raw_data = load_insights_data(FILEPATH)
        print_sample_data(raw_data)

        # Normalizar os dados
        normalized_data = normalize_data(raw_data)
        print(f"Dados normalizados. Total de registros: {len(normalized_data)}.")
        if normalized_data:
            print(f"Exemplo de dado normalizado: {normalized_data[0]}")

        # Validar a existência das chaves esperadas antes de acessar
        print("\nValidando estrutura dos dados:")
        for item in normalized_data[:5]:  # Limitar a amostra para não imprimir tudo
            adset_id = item.get("adset_id", "Chave ausente")
            date_start = item.get("date_start", "Chave ausente")
            date_stop = item.get("date_stop", "Chave ausente")
            print(f"Adset ID: {adset_id}, Date Start: {date_start}, Date Stop: {date_stop}")

        # Testar a filtragem
        print("\nTestando filtragem:")
        filtered_data = filter_data(
            normalized_data,
            adset_id="23849164162230688",  # Um valor que está no JSON
            date_start="2022-01-01",
            date_stop="2022-01-02"
        )
        print(f"Dados filtrados: {len(filtered_data)} registros encontrados.")
        if filtered_data:
            print(f"Exemplo de dado filtrado: {filtered_data[0]}")
        else:
            print("Nenhum dado corresponde aos critérios de filtragem.")

    except Exception as e:
        print(f"Erro durante o teste: {e}")

# Executar os testes
if __name__ == "__main__":
    run_tests()
