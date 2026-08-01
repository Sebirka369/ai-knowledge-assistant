from app.database.session import SessionLocal
from app.services.embedding_pipeline import EmbeddingPipeline


db = SessionLocal()

try:
    pipeline = EmbeddingPipeline(db)

    count = pipeline.rebuild()

    print(f"Rebuilt embeddings for {count} chunks.")

finally:
    db.close()
