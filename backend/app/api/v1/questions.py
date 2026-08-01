from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.question import QuestionRequest
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.post("/")
def ask_question(
    request: QuestionRequest,
    db: Session = Depends(get_db),
):
    service = RAGService(db)

    answer = service.answer(
        question=request.question,
        document_id=request.document_id,
    )

    return {
        "question": request.question,
        "document_id": request.document_id,
        "answer": answer,
    }
