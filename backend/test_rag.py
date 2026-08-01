from app.database.session import SessionLocal
from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService


db = SessionLocal()

try:
    question = "What is the goal of this roadmap?"
    document_id = 4

    retrieval_service = RetrievalService(db)

    chunks = retrieval_service.retrieve(
        question=question,
        document_id=document_id,
        limit=5,
    )

    context = "\n\n".join(
        chunk["content"]
        for chunk in chunks
    )

    print(f"Number of chunks: {len(chunks)}")
    print(f"Context length: {len(context)} characters")
    print("=" * 80)
    print(context)
    print("=" * 80)

    llm_service = LLMService()

    answer = llm_service.generate(
        question=question,
        context=context,
    )

    print("Answer:")
    print(answer)

finally:
    db.close()