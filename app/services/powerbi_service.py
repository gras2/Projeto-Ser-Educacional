"""
Serviço responsável por enviar dados ao Power BI.
- Funções principais:
  - Preparar dados para envio.
  - Integrar com a API REST do Power BI.
"""
import httpx
import pandas as pd
from loguru import logger
