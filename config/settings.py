from pydantic import BaseSettings, Field, ValidationError  # Importa classes e funções do Pydantic para validação e leitura de configurações

# Definindo a classe Settings, que herda de BaseSettings
class Settings(BaseSettings):
    # Define a variável META_ADS_TOKEN que será lida do ambiente
    META_ADS_TOKEN: str = Field(..., env="META_ADS_TOKEN")  # O '...' indica que a variável é obrigatória no arquivo .env ou no ambiente

    # POWERBI_TOKEN: str = Field(..., env="POWERBI_TOKEN")  

    # Define uma versão padrão da API, caso não seja especificada
    API_VERSION: str = "v1"  # A versão da API será "v1", a menos que seja alterada no ambiente

    # A classe Config dentro de Settings define o arquivo de ambiente (.env) e a codificação do arquivo
    class Config:
        env_file = ".env"  # Arquivo que contém as variáveis de ambiente
        env_file_encoding = "utf-8"  # Codificação do arquivo de ambiente (UTF-8)

# Tenta carregar as configurações, se não for possível, gera um erro de runtime
try:
    settings = Settings()  # Tenta instanciar a classe Settings e carregar as variáveis do arquivo .env
except ValidationError as e:
    # Caso haja algum erro de validação (ex: falta de variáveis obrigatórias), lança uma exceção com a mensagem de erro
    raise RuntimeError(f"Erro nas configurações: {e}")
