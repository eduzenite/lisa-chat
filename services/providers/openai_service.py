from openai import OpenAI
from core.config import settings

class OpenAIService:
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY não encontrada no .env")

        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def ask(self, question: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        # Aqui está o ajuste correto
        return response.choices[0].message.content
