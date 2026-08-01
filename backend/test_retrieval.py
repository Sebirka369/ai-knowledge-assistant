from app.database.session import SessionLocal
from app.services.retrieval_service import RetrievalService

db = SessionLocal()

try:
    service = RetrievalService(db)

    question = "What is this document about?"

    results = service.retrieve(
        question=question,
        document_id=4,
        limit=5,
    )

    print(f"Question: {question}")
    print("Document ID: 4")
    print()

    for result in results:
        print("Chunk ID:", result["chunk_id"])
        print("Document ID:", result["document_id"])
        print("Chunk Index:", result["chunk_index"])
        print("Distance:", result["distance"])
        print("Content:")
        print(result["content"])
        print("=" * 80)

finally:
    db.close()
