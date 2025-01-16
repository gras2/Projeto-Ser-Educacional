from pydantic_settings import BaseSettings  # BaseSettings agora está no pacote pydantic-settings
from pydantic import Field, ValidationError  # Field e ValidationError continuam no Pydantic principal

# Definindo a classe Settings, que herda de BaseSettings
class Settings(BaseSettings):
    # Define a variável META_ADS_ACCESS_TOKEN que será lida do ambiente
    META_ADS_ACCESS_TOKEN: str = Field(..., env="META_ADS_ACCESS_TOKEN")  # O '...' indica que a variável é obrigatória no arquivo .env ou no ambiente

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
