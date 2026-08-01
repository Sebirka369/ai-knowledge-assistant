from app.database.session import SessionLocal
from app.repositories.chunk_repository import ChunkRepository

db = SessionLocal()

try:
    repository = ChunkRepository(db)

    chunk = repository.get_by_id(19)

    if chunk:
        print("Chunk found")
        print("ID:", chunk.id)
        print("Document ID:", chunk.document_id)
        print("Chunk index:", chunk.chunk_index)
        print("Content:")
        print(chunk.content)
    else:
        print("Chunk not found")

finally:
    db.close()
