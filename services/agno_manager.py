from services.providers.openai_service import OpenAIService
from services.providers.gemini_service import GeminiService
from services.providers.claude_service import ClaudeService

class AgnoManager:
    def __init__(self):
        self.providers = {
            "openai": OpenAIService(),
            "gemini": GeminiService(),
            "claude": ClaudeService()
        }

    async def ask(self, provider_name: str, question: str):
        provider = self.providers.get(provider_name)

        if not provider:
            raise ValueError(f"Provider {provider_name} não configurado")

        return await provider.ask(question)
