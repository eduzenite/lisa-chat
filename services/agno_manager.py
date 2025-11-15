from sqlalchemy.orm import Session
from services.sql_ai_service import SQLAIService

class AgnoManager:
    def __init__(self, db: Session):
        self.sql_ai = SQLAIService(db)

    def ask_db(self, question: str) -> str:
        return self.sql_ai.ask(question)
