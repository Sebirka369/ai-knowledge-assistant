from sqlalchemy.orm import Session

from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGService:

    def __init__(
        self,
        db: Session,
    ):
        self.retrieval_service = RetrievalService(db)
        self.llm_service = LLMService()

    def answer(
        self,
        question: str,
        document_id: int,
        limit: int = 5,
    ) -> str:

        chunks = self.retrieval_service.retrieve(
            question=question,
            document_id=document_id,
            limit=limit,
        )

        context = "\n\n".join(
            chunk["content"]
            for chunk in chunks
        )

        return self.llm_service.generate(
            question=question,
            context=context,
        )
