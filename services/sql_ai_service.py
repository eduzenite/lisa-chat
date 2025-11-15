from sqlalchemy.orm import Session
from sqlalchemy import text, inspect
from services.providers.openai_service import OpenAIService

class SQLAIService:
    def __init__(self, db: Session):
        self.db = db
        self.ai = OpenAIService()
        self.inspector = inspect(db.bind)

    def get_schema_description(self) -> str:
        description = ""
        for table_name in self.inspector.get_table_names():
            columns = [col['name'] for col in self.inspector.get_columns(table_name)]
            description += f"Tabela {table_name}: colunas {columns}\n"
        return description

    def ask(self, question: str) -> str:
        """
        Recebe pergunta em linguagem natural, gera SQL, executa e retorna resposta pronta.
        """
        schema_description = self.get_schema_description()

        # 1️⃣ Gera SQL usando IA
        prompt_sql = f"""
        Você é um assistente que gera consultas SQL para MySQL.
        Base de dados:
        {schema_description}
        Pergunta: {question}
        Retorne apenas o SQL válido.
        """
        sql_query = self.ai.get_sql(prompt_sql)

        try:
            # 2️⃣ Executa a SQL no banco
            result = self.db.execute(text(sql_query)).fetchall()

            # 3️⃣ Formata resultado em linguagem natural
            prompt_answer = f"""
            Você é um assistente que transforma resultados de SQL em respostas curtas e claras.
            Pergunta: {question}
            Resultado da query: {result}
            Responda de forma objetiva.
            """
            answer = self.ai.get_text(prompt_answer)
            return answer

        except Exception as e:
            return f"Erro ao executar a query: {e}"
