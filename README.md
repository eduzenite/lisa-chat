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
sqlacodegen mysql+pymysql://root:12345678@localhost:3306/banco_de_dados --outfile models/models.py
```

## 🔐 Configuração do .env

Crie um arquivo `.env`:

    OPENAI_API_KEY=sua_chave
    GEMINI_API_KEY=sua_chave
    CLAUDE_API_KEY=sua_chave
    DATABASE_URL=mysql+pymysql://root:12345678@localhost:3306/banco_de_dados

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

    api/
    ├─ v1/
       ├─ __init__.py
       └─ ai_routes.py
    ├─ __init__.py
    └─ routes.py
    ├─ core/
    ├─ __init__.py
    ├─ config.py
    └─ database.py
    ├─ models/
    ├─ __init__.py
    └─ schemas.py
    ├─ services/
    └─ providers/
       ├─ __init__.py
       ├─ openai_service.py
       ├─ gemini_service.py
       └─ claude_service.py
    ├─ __init__.py
    ├─ agno_manager.py
    └─ ai_service.py
    .env
    .gitignore
    __init__.py
    main.py
    README.md
    requirements.txt
    test_main.http
