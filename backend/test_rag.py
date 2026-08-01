from app.database.session import SessionLocal
from app.services.rag_service import RAGService

db = SessionLocal()

try:
    service = RAGService(db)

    question = "What is this document about?"

    answer = service.answer(
        question=question,
        document_id=4,
        limit=5,
    )

    print("Question:")
    print(question)

    print("\nAnswer:")
    print(answer)

finally:
    db.close()
