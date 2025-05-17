
# 🧠 Nutri AI + Shopify Integration

Este projeto tem como objetivo integrar a **Nutri AI** com a **plataforma Shopify**, permitindo que a IA converse com os clientes, colete informações nutricionais, sugira dietas personalizadas e indique produtos da loja Shopify compatíveis com a dieta.

---

## ✅ Objetivo

- Coletar dados do cliente via chat
- Gerar uma dieta personalizada com OpenAI
- Buscar produtos compatíveis na loja Shopify
- Retornar sugestão + links dos produtos
- Registrar histórico para melhorias futuras

---

## 🔧 Tecnologias e Ferramentas Envolvidas

| Finalidade                      | Ferramenta                              |
|-------------------------------|------------------------------------------|
| LLM / Geração de texto        | OpenAI GPT-4 / Anthropic Claude / Gemini|
| Backend API                   | Node.js (Express) ou Python (FastAPI)    |
| Integração com Shopify        | Shopify REST ou GraphQL API              |
| Integração no WhatsApp        | Twilio, Gupshup, 360dialog ou Z-API      |
| Chat no site (opcional)       | Tidio, Crisp, Chatwoot, Botpress         |
| Base de dados                 | Firebase, PostgreSQL, MongoDB            |

---

## 🧩 Como Funciona na Prática (Arquitetura)

### 🔁 Fluxo Resumido

```
Usuário (WhatsApp/Web) → Backend (FastAPI) → OpenAI (Chat) + Banco (Contexto)
                                            ↘
                                             Shopify API (Consulta de Produtos)
```

### 📈 Fluxograma

```
[Usuário Inicia Conversa]
        ↓
[Backend recebe mensagem]
        ↓
[Verifica se há histórico no DB]
        ↓
[Envio do contexto para OpenAI]
        ↓
[IA responde e sugere dieta]
        ↓
[Backend busca produtos na Shopify]
        ↓
[IA finaliza com links dos produtos]
        ↓
[Salva dieta e resposta no DB]
```

---

## 📁 Estrutura de Diretórios (Python + FastAPI)

```
nutri_ai_shopify/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── chat.py
│   │   └── products.py
│   ├── services/
│   │   ├── openai_service.py
│   │   └── shopify_service.py
│   ├── schemas/
│   │   └── chat_schema.py
│   ├── utils/
│   │   └── context_manager.py
│   └── db/
│       └── database.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Bibliotecas Que serão utilizadas

| Finalidade                   | Biblioteca                             |
|-----------------------------|-----------------------------------------|
| Web framework               | `fastapi`, `uvicorn`                    |
| OpenAI                      | `openai`                                |
| Shopify API                 | `shopifyapi` ou `requests` com tokens   |
| Banco de dados              | `motor` (Mongo) ou `sqlalchemy` (SQL)   |
| Validação                   | `pydantic`                              |
| Variáveis ambiente          | `python-dotenv`                         |
| Autenticação (se for o caso)| `httpx`, `jwt`, `oauthlib`              |

---

## 🧪 Código Inicial

### 📍 `main.py`

```python
from fastapi import FastAPI
from app.routes import chat, products

app = FastAPI()
app.include_router(chat.router)
app.include_router(products.router)
```

### 📍 `routes/chat.py`

```python
from fastapi import APIRouter, Request
from app.services.openai_service import gerar_resposta
from app.services.shopify_service import buscar_produtos

router = APIRouter()

@router.post("/chat")
async def chat_interativo(request: Request):
    body = await request.json()
    mensagem = body["mensagem"]
    contexto = body.get("contexto", [])
    
    resposta_ia = gerar_resposta(mensagem, contexto)
    produtos_sugeridos = buscar_produtos(resposta_ia)

    return {"resposta": resposta_ia, "produtos": produtos_sugeridos}
```

### 📍 `services/openai_service.py`

```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(mensagem, contexto):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é uma nutricionista que cria dietas."},
            *contexto,
            {"role": "user", "content": mensagem}
        ]
    )
    return completion["choices"][0]["message"]["content"]
```

### 📍 `services/shopify_service.py`

```python
import requests
import os

SHOPIFY_URL = os.getenv("SHOPIFY_API_URL")
TOKEN = os.getenv("SHOPIFY_API_TOKEN")

def buscar_produtos(texto):
    termos = extrair_ingredientes(texto)  # função simples que você pode criar
    produtos = []
    for termo in termos:
        res = requests.get(f"{SHOPIFY_URL}/products.json?title={termo}", headers={
            "X-Shopify-Access-Token": TOKEN
        })
        produtos += res.json().get("products", [])
    return produtos
```

---

## ✅ Próximos Passos

1. Integrar à loja Shopify com produtos tagueados
2. Configurar `.env` com as chaves da OpenAI e Shopify
3. Escolher canal de entrada (WhatsApp, chat etc.)
4. Ajustar prompt do modelo para alta performance
5. Armazenar histórico de usuários e dietas

---

Se quiser ajuda com a implementação de qualquer etapa, posso entregar os módulos separados ou o projeto inteiro em repositório pronto.
