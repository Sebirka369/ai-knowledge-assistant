from sqlalchemy.orm import Session

from app.repositories.chunk_repository import ChunkRepository
from app.services.embedding_service import EmbeddingService
from app.vector_store.milvus import MilvusStore


class RetrievalService:

    def __init__(
        self,
        db: Session,
    ):
        self.chunk_repository = ChunkRepository(db)
        self.embedder = EmbeddingService()
        self.vector_store = MilvusStore()

    def retrieve(
        self,
        question: str,
        limit: int = 5,
        document_id: int | None = None,
    ) -> list[dict]:

        query_embedding = self.embedder.create_embedding(question)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit,
            document_id=document_id,
        )

        hits = results[0]

        chunk_ids = [int(hit["entity"]["chunk_id"]) for hit in hits]

        chunks = self.chunk_repository.get_by_ids(chunk_ids)

        chunks_by_id = {chunk.id: chunk for chunk in chunks}

        retrieved_chunks = []

        for hit in hits:
            chunk_id = int(hit["entity"]["chunk_id"])

            chunk = chunks_by_id.get(chunk_id)

            if chunk is None:
                continue

            retrieved_chunks.append(
                {
                    "chunk_id": chunk.id,
                    "document_id": chunk.document_id,
                    "chunk_index": chunk.chunk_index,
                    "content": chunk.content,
                    "distance": hit["distance"],
                }
            )

        return retrieved_chunks
