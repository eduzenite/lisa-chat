# 📘 README --- Projeto FastAPI com Arquitetura para IA

Este é um projeto FastAPI estruturado para trabalhar com múltiplos
provedores de IA por meio de um gerenciador central (Agno Manager).\
A arquitetura separa:

-   Camada Web (FastAPI / Rotas)
-   Camada de Serviços (OpenAI, Gemini, Claude)
-   Gerenciador de IA (AgnoManager)
-   Configurações (.env)

## 🚀 Requisitos

-   Python 3.11+
-   Git
-   Ambiente virtual
-   Chaves de API (OpenAI, Gemini, Claude)

## 🔧 Instalação

``` sh
git clone git@github.com:eduzenite/lisa-chat.git
cd lisa-chat
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🔐 Configuração do .env

Crie um arquivo `.env`:

    OPENAI_API_KEY=sua_chave
    GEMINI_API_KEY=sua_chave
    CLAUDE_API_KEY=sua_chave

## ▶️ Executando

``` sh
uvicorn app.main:app --reload
```

## 🧪 Testando

POST `/ai/ask`:

``` json
{
  "provider": "openai",
  "question": "Explique o que é FastAPI"
}
```

## 🏗️ Estrutura

    app/
    ├─ api/
    │  └─ ai.py
    ├─ core/
    │  └─ config.py
    ├─ services/
    │  ├─ agno_manager.py
    │  └─ providers/
    │     ├─ openai_service.py
    │     ├─ gemini_service.py
    │     └─ claude_service.py
    main.py
