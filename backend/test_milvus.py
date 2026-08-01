from app.vector_store.milvus import MilvusStore


store = MilvusStore()

store.create_index()

store.load_collection()

result = store.client.query(
    collection_name=store.COLLECTION_NAME,
    filter="",
    output_fields=[
        "chunk_id",
        "document_id",
        "chunk_index",
    ],
    limit=100,
)

print(f"Number of vectors: {len(result)}")

for item in result:
    print(item)
