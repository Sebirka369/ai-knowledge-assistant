from app.services.embedding_service import EmbeddingService
from app.vector_store.milvus import MilvusStore

question = "What is this document about?"

embedder = EmbeddingService()

query_embedding = embedder.create_embedding(question)

store = MilvusStore()

store.load_collection()

search_results = store.search(
    query_embedding=query_embedding,
    limit=5,
)

print(f"Question: {question}")
print()

for hits in search_results:
    for hit in hits:
        print(
            {
                "distance": hit["distance"],
                "chunk_id": hit["entity"]["chunk_id"],
                "document_id": hit["entity"]["document_id"],
                "chunk_index": hit["entity"]["chunk_index"],
            }
        )
