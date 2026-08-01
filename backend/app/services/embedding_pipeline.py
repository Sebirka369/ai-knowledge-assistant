from sqlalchemy.orm import Session

from app.repositories.chunk_repository import ChunkRepository
from app.services.embedding_service import EmbeddingService
from app.vector_store.milvus import MilvusStore


class EmbeddingPipeline:

    def __init__(
        self,
        db: Session,
    ):
        self.chunk_repository = ChunkRepository(db)
        self.embedder = EmbeddingService()
        self.vector_store = MilvusStore()

    def rebuild(self):
        chunks = self.chunk_repository.get_all()

        self.vector_store.drop_collection()
        self.vector_store.create_collection()
        self.vector_store.create_index()
        self.vector_store.load_collection()

        for chunk in chunks:
            embedding = self.embedder.create_embedding(
                chunk.content
            )

            self.vector_store.insert_chunk(
                chunk_id=str(chunk.id),
                document_id=str(chunk.document_id),
                chunk_index=chunk.chunk_index,
                embedding=embedding,
            )

        return len(chunks)
