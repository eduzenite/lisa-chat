from core.config import settings

class GeminiService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY

    async def ask(self, question: str) -> str:
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY não encontrada no .env")

        return f"[Gemini] Resposta para: {question}"
