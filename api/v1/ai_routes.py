from fastapi import APIRouter
from pydantic import BaseModel
from services.agno_manager import AgnoManager

router = APIRouter(prefix="/ai")

class QuestionRequest(BaseModel):
    provider: str
    question: str

class AnswerResponse(BaseModel):
    answer: str

agno = AgnoManager()

@router.post("/ask", response_model=AnswerResponse)
async def ask_ai(req: QuestionRequest):
    answer = await agno.ask(req.provider, req.question)
    return {"answer": answer}
