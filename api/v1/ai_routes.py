from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.agno_manager import AgnoManager
from core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/ai")

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AnswerResponse)
def ask_db(
    request: QuestionRequest,
    db: Session = Depends(get_db)
):
    agno = AgnoManager(db)
    answer = agno.ask_db(request.question)
    return AnswerResponse(answer=answer)
