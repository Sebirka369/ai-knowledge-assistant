from app.database.session import SessionLocal
from app.services.retrieval_service import RetrievalService


db = SessionLocal()

try:
    service = RetrievalService(db)

    question = "What is the goal of this roadmap?"

    results = service.retrieve(
        question=question,
        document_id=4,
        limit=5,
    )

    print(f"Question: {question}")
    print("Document ID: 4")
    print("=" * 80)

    for result in results:
        print(f"Chunk ID: {result['chunk_id']}")
        print(f"Document ID: {result['document_id']}")
        print(f"Chunk Index: {result['chunk_index']}")
        print(f"Distance: {result['distance']}")
        print(f"Content: {result['content'][:200]}")
        print("=" * 80)

finally:
    db.close()