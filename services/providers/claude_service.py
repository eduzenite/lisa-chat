from core.config import settings

class ClaudeService:
    def __init__(self):
        self.api_key = settings.CLAUDE_API_KEY

    async def ask(self, question: str) -> str:
        if not self.api_key:
            raise RuntimeError("CLAUDE_API_KEY não encontrada no .env")

        return f"[Claude] Resposta para: {question}"
